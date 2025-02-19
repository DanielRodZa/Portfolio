from DepthEstimator import DepthEstimator
import argparse

def main():
    parser = argparse.ArgumentParser(description='Genera un mara de profundidad para imágenes usando MiDas')
    parser.add_argument("input_dir", help="Directorio donde se encuentran las imágenes")
    parser.add_argument("output_dir", help="Directorio donde guardar los maps")
    parser.add_argument("-m","--model",
                        help="Tipo de modelo MiDas (DPT_Large, DPT_Hybrid, MiDaS_small). Por defecto: DPT_Large.",
                        default="DPT_Large",
                        dest="model_type")
    args = parser.parse_args()

    depth_estimator = DepthEstimator(args.model_type)
    depth_estimator.process_image(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()