from project_reasoner.good_vibrations.types import GV


def test_prompt_template_type():
    assert (
        str(GV.prompt_template) == "https://good.vibrations.dev/types/prompt_template"
    )
