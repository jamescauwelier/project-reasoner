from project_reasoner.prompt.template import create_prompt_template


def test_prompt_templates_have_an_id_property():
    template = create_prompt_template()
    assert template.id is not None


def test_prompt_templates_have_a_name_property():
    pass


def test_prompt_templates_have_a_contents_property():
    pass


def test_prompt_templates_have_a_parameters_property():
    pass
