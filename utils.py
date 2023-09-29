def prepare_payload(prompt: str) -> dict:
    """Create a payload for the stable diffusion API.

    Args:
        prompt (str): prompt for the image generation.

    Returns:
        dict: payload dictionary.
    """
    payload = {
        "alwayson_scripts": {
            "API payload": {"args": []},
            "Extra options": {"args": []},
            "Refiner": {"args": [False, "", 0.8]},
            "Seed": {"args": [-1, False, -1, 0, 0, 0]},
        },
        "batch_size": 1,
        "cfg_scale": 7,
        "comments": {},
        "disable_extra_networks": False,
        "do_not_save_grid": False,
        "do_not_save_samples": False,
        "enable_hr": False,
        "height": 512,
        "hr_negative_prompt": "",
        "hr_prompt": "",
        "hr_resize_x": 0,
        "hr_resize_y": 0,
        "hr_scale": 2,
        "hr_second_pass_steps": 5,
        "hr_upscaler": "Latent",
        "n_iter": 1,
        "negative_prompt": "",
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "prompt": prompt,
        "restore_faces": False,
        "s_churn": 0,
        "s_min_uncond": 0,
        "s_noise": 1,
        "s_tmax": None,
        "s_tmin": 0,
        "sampler_name": "DPM++ 2M Karras",
        "script_args": [],
        "script_name": None,
        "seed": -1,
        "seed_enable_extras": True,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "steps": 10,
        "styles": [],
        "subseed": -1,
        "subseed_strength": 0,
        "tiling": False,
        "width": 512,
    }

    return payload
