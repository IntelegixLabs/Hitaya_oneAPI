import numpy as np
import cv2
from datetime import datetime
import torch
import torch.backends.cudnn as cudnn
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, non_max_suppression, scale_coords, set_logging
from utils.plots import plot_one_box
from utils.torch_utils import select_device


def chest_xray(source="0", model_weights="resources/models/chest_xray.pt"):

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    weights = model_weights

    img_size = 640
    iou_thres = 0.45
    conf_thres = 0.5

    font = cv2.FONT_HERSHEY_SIMPLEX

    webcam = source.isnumeric()

    # Initialize
    set_logging()
    device = select_device(device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(img_size, s=stride)  # check img_size

    if half:
        model.half()  # to FP16

    # Set Dataloader
    if webcam:
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    print(names)

    # colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)
    #     , (155, 255, 100), (255, 155, 100), (155, 100, 255), (155, 155, 100)]

    colors = [[np.random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    old_img_w = old_img_h = imgsz
    old_img_b = 1

    TOTAL = 0
    Aortic_enlargement = 0
    Atelectasis = 0
    Calcification = 0
    Cardiomegaly = 0
    Consolidation = 0
    ILD = 0
    Infiltration = 0
    Lung_Opacity = 0
    Nodule_Mass = 0
    Other_lesion = 0
    Pleural_effusion = 0
    Pleural_thickening = 0
    Pneumothorax = 0
    Pulmonary_fibrosis = 0

    predictions = []
    for path, img, im0s, vid_cap in dataset:

        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Warmup
        if device.type != 'cpu' and (
                old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
            old_img_b = img.shape[0]
            old_img_h = img.shape[2]
            old_img_w = img.shape[3]

        # Inference
        with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
            pred = model(img)[0]

        # Apply NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres)

        # Process detections
        current_frame_detector = 0
        for i, det in enumerate(pred):  # detections per image

            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            im0 = cv2.resize(im0, (640, 480))

            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()


                # Write results

                for *xyxy, conf, cls in reversed(det):


                    print(cls)
                    label = f'{names[int(cls)]} {conf:.2f}'
                    print(label)
                    current_frame_detector += 1
                    labelx = names[int(cls)]
                    # data_type, confidence = label.split(" ")

                    if labelx == 'Aortic enlargement':
                        plot_one_box(xyxy, im0, label=label, color=colors[0], line_thickness=1)
                        Aortic_enlargement += 1
                    elif labelx == 'Atelectasis':
                        plot_one_box(xyxy, im0, label=label, color=colors[1], line_thickness=1)
                        Atelectasis += 1
                    elif labelx == 'Calcification':
                        plot_one_box(xyxy, im0, label=label, color=colors[2], line_thickness=1)
                        Calcification += 1
                    elif labelx == 'Cardiomegaly':
                        plot_one_box(xyxy, im0, label=label, color=colors[3], line_thickness=1)
                        Cardiomegaly += 1
                    elif labelx == 'Consolidation':
                        plot_one_box(xyxy, im0, label=label, color=colors[4], line_thickness=1)
                        Consolidation += 1
                    elif labelx == 'ILD':
                        plot_one_box(xyxy, im0, label=label, color=colors[5], line_thickness=1)
                        ILD += 1
                    elif labelx == 'Infiltration':
                        plot_one_box(xyxy, im0, label=label, color=colors[6], line_thickness=1)
                        Infiltration += 1
                    elif labelx == 'Lung Opacity':
                        plot_one_box(xyxy, im0, label=label, color=colors[7], line_thickness=1)
                        Lung_Opacity += 1
                    elif labelx == 'Nodule/Mass':
                        plot_one_box(xyxy, im0, label=label, color=colors[8], line_thickness=1)
                        Nodule_Mass += 1
                    elif labelx == 'Other lesion':
                        plot_one_box(xyxy, im0, label=label, color=colors[9], line_thickness=1)
                        Other_lesion += 1
                    elif labelx == 'Pleural effusion':
                        plot_one_box(xyxy, im0, label=label, color=colors[10], line_thickness=1)
                        Pleural_effusion += 1
                    elif labelx == 'Pleural thickening':
                        plot_one_box(xyxy, im0, label=label, color=colors[10], line_thickness=1)
                        Pleural_thickening += 1
                    elif labelx == 'Pneumothorax':
                        plot_one_box(xyxy, im0, label=label, color=colors[10], line_thickness=1)
                        Pneumothorax += 1
                    elif labelx == 'Pulmonary fibrosis':
                        plot_one_box(xyxy, im0, label=label, color=colors[10], line_thickness=1)
                        Pulmonary_fibrosis += 1


                    x = (int(xyxy[0]))
                    y = (int(xyxy[1]))
                    w = (int(xyxy[2]))
                    h = (int(xyxy[3]))

                    roi = im0[y:h, x:w]
                    # roi = roi / 255.0
                    # # step-05: resize images (100,100)
                    # if roi.shape[1] > 100:
                    #     roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_AREA)
                    # else:
                    #     roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_CUBIC)



                    output = {
                        'roi': roi,
                        'x': (int(xyxy[0])),
                        'y': (int(xyxy[1])),
                        'w': (int(xyxy[2])),
                        'h': (int(xyxy[3])),
                        'prediction_class': names[int(cls)],
                        'prediction_score': f'{conf:.2f}',
                    }

                    predictions.append(output)

            (H, W) = im0.shape[:2]


            cv2.putText(im0, "Hitaya One", (260, 40),
                        font, 0.7 * 1, (255, 255, 255), 2)
            cv2.rectangle(im0, (20, 50), (W - 20, 15), (255, 255, 255), 2)

            sub_img = im0[H - 350: H, 0:200]
            black_rect = np.ones(sub_img.shape, dtype=np.uint8) * 0

            res = cv2.addWeighted(sub_img, 0.8, black_rect, 0.2, 1.0)

            im0[H - 350:H + 40, 0:200] = res

            cv2.putText(im0, str("Pneumothorax: " + str(Pneumothorax)), (30, H - 330),
                        font, 0.4 * 1, colors[12], 1)
            cv2.rectangle(im0, (10, H - 330), (20, H - 335), colors[12], 7)

            cv2.putText(im0, str("Pulmonary fibrosis: " + str(Pulmonary_fibrosis)), (30, H - 305),
                        font, 0.4 * 1, colors[13], 1)
            cv2.rectangle(im0, (10, H - 305), (20, H - 310), colors[13], 7)

            cv2.putText(im0, str("Aortic enlargement: " + str(Aortic_enlargement)), (30, H - 280),
                        font, 0.4 * 1, colors[0], 1)
            cv2.rectangle(im0, (10, H - 280), (20, H - 285), colors[0], 7)

            cv2.putText(im0, str("Atelectasis: " + str(Atelectasis)), (30, H - 255),
                        font, 0.4 * 1, colors[1], 1)
            cv2.rectangle(im0, (10, H - 255), (20, H - 260), colors[1], 7)

            cv2.putText(im0, str("Calcification: " + str(Calcification)), (30, H - 230),
                        font, 0.4 * 1, colors[2], 1)
            cv2.rectangle(im0, (10, H - 230), (20, H - 235), colors[2], 7)

            cv2.putText(im0, str("Cardiomegaly: " + str(Cardiomegaly)), (30, H - 205),
                        font, 0.4 * 1, colors[3], 1)
            cv2.rectangle(im0, (10, H - 205), (20, H - 210), colors[3], 7)

            cv2.putText(im0, str("Consolidation: " + str(Consolidation)), (30, H - 180),
                        font, 0.4 * 1, colors[4], 1)
            cv2.rectangle(im0, (10, H - 180), (20, H - 185), colors[4], 7)

            cv2.putText(im0, str("ILD: " + str(ILD)), (30, H - 155),
                        font, 0.4 * 1, colors[5], 1)
            cv2.rectangle(im0, (10, H - 155), (20, H - 160), colors[5], 7)

            cv2.putText(im0, str("Infiltration: " + str(Infiltration)), (30, H - 130),
                        font, 0.4 * 1, colors[6], 1)
            cv2.rectangle(im0, (10, H - 130), (20, H - 135), colors[6], 7)

            cv2.putText(im0, str("Lung Opacity: " + str(Lung_Opacity)), (30, H - 105),
                        font, 0.4 * 1, colors[7], 1)
            cv2.rectangle(im0, (10, H - 105), (20, H - 100), colors[7], 7)

            cv2.putText(im0, str("Nodule/Mass: " + str(Nodule_Mass)), (30, H - 80),
                        font, 0.4 * 1, colors[8], 1)
            cv2.rectangle(im0, (10, H - 80), (20, H - 85), colors[8], 7)

            cv2.putText(im0, str("Other lesion: " + str(Other_lesion)), (30, H - 55),
                        font, 0.4 * 1, colors[9], 1)
            cv2.rectangle(im0, (10, H - 55), (20, H - 60), colors[9], 7)

            cv2.putText(im0, str("Pleural effusion: " + str(Pleural_effusion)), (30, H - 30),
                        font, 0.4 * 1, colors[10], 1)
            cv2.rectangle(im0, (10, H - 30), (20, H - 35), colors[10], 7)

            cv2.putText(im0, str("Pleural effusion: " + str(Pleural_effusion)), (30, H - 5),
                        font, 0.4 * 1, colors[11], 1)
            cv2.rectangle(im0, (10, H - 5), (20, H - 10), colors[11], 7)



            cv2.putText(im0, str("CURRENT FRAME: " + str(current_frame_detector)), (W - 225, H - 35),
                        font, 0.7 * 1, (0, 0, 255), 2)

            now = datetime.now()

            timex = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            cv2.putText(im0, timex, (W - 200, H - 10),
                        font, 0.5 * 1, (255, 255, 255), 1)

            return im0, predictions