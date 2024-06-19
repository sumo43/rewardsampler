from vllm import LLM, SamplingParams

def load_vllm_generator_model(model_name: str, sampling_params: SamplingParams):
    """
        We use vLLM for the generator model, since we need high throughput here.
    """
    model = vllm.


def load_hf_bert_reward_model(model_name):



if __name__ == "__main__":