from har.impl.lstm_simple.train import train
from har.utils.dataset_util import get_berkeley_dataset, SetType, berkeley_mhad_classes, video_pose_3d_kpts, DatasetInputType, \
    GeometricFeature


def main():
    training_data, training_labels = get_berkeley_dataset('datasets_processed/berkeley/3D', set_type=SetType.TRAINING)
    validation_data, validation_labels = get_berkeley_dataset('datasets_processed/berkeley/3D', set_type=SetType.VALIDATION)

    train(berkeley_mhad_classes, training_data, training_labels, validation_data, validation_labels, video_pose_3d_kpts,
          epoch_nb=3000)


if __name__ == '__main__':
    main()
