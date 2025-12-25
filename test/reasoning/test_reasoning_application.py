from project_reasoner.reasoning.application import ReasoningApplication


class TestApplication:

    def test_a_reasoning_application_can_be_initialized(self):
        app = TestApplication.create(name="Project Analysis Application")
        assert app.name == "Project Analysis Application"

    @staticmethod
    def create(name: str = "Test Application") -> ReasoningApplication:
        return ReasoningApplication(name=name)
