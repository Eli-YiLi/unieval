import os
import torch

from transformers import PretrainedConfig, PreTrainedModel

from .base_projector import MultimodalProjectorConfig, MultimodalProjector


def build_mm_projector(
    model_type_or_path: str, config: PretrainedConfig
) -> PreTrainedModel:
    if model_type_or_path is None:
        return None

    if config.resume_path:
        assert os.path.exists(
            model_type_or_path
        ), f"Resume mm projector path {model_type_or_path} does not exist!"
        return MultimodalProjector.from_pretrained(
            model_type_or_path, config, torch_dtype=eval(config.model_dtype)
        )
    else:
        mm_projector_cfg = MultimodalProjectorConfig(model_type_or_path)
        mm_projector = MultimodalProjector(mm_projector_cfg, config).to(
            eval(config.model_dtype)
        )
        return mm_projector