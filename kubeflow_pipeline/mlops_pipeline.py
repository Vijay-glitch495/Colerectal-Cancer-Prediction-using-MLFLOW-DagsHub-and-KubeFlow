import kfp
from kfp import dsl


@dsl.container_component
def data_processing_op():
    return dsl.ContainerSpec(
        image='vijaydocker27915/my-mlops-app',
        command=['python', 'src/data_processing.py']
    )


@dsl.container_component
def data_model_training_op():
    return dsl.ContainerSpec(
        image='vijaydocker27915/my-mlops-app',
        command=['python', 'src/model_training.py']
    )


@dsl.pipeline(
    name='MLOps Pipeline',
    description='An example MLOps pipeline for colorectal cancer prediction'
)
def mlops_pipeline():
    data_processing = data_processing_op()
    data_model_training_op().after(data_processing)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=mlops_pipeline,
        package_path="mlops_pipeline.yaml"
    )
    print("Pipeline compiled successfully.")