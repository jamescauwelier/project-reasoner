from dataclasses import dataclass
from typing import Dict, Optional

type Label = str
type DataType = str


@dataclass(frozen=True)
class CreatePromptTemplateCommand:
    name: str
    template: str
    parameter_definitions: Optional[Dict[Label, DataType]]
