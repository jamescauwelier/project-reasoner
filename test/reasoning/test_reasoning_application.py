from project_reasoner.reasoning.application import ReasoningApplication


def test_a_reasoning_application_can_be_initialized():
    app = ReasoningApplication(name="Project Analysis Application")
    assert app.name == "Project Analysis Application"
