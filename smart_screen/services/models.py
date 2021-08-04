from django.db import models
from enum import Enum
from typing import List, Dict, Sequence, Optional
from dataclasses import dataclass

class ImageTypes(Enum):
    LOGO = "logo"
    BANNER = "banner"
    SPOTLIGHT = "spotlight"

@dataclass
class TextLocale:
    language: str
    value: str

@dataclass
class TitleAndDesc:
    default: str
    locales: Optional[Sequence[TextLocale]]

@dataclass
class Tags:
    categories: Optional[List[str]]
    keywords: Optional[List[str]]

@dataclass
class ImageValue:
    id: str
    etag: str

@dataclass
class ImageLocale:
    language: str
    value: ImageValue

@dataclass
class ImageWithLocales:
    default: ImageValue
    locales: Optional[Sequence[ImageLocale]]


@dataclass
class LaunchInstructions:
    chatRecipient: Optional[str]
    callbackUrl: Optional[str]

class Service:
    title: TitleAndDesc
    description: TitleAndDesc
    launchInstructions: LaunchInstructions
    type: str
    behaviour: str
    tags: Tags
    requirements: Dict[str, str]
    logo: ImageValue
    banner: Optional[ImageWithLocales]
    spotlight: Optional[ImageWithLocales]

    def __init__(self, data: Dict) -> None:
        self.title = data.get("title")
        self.description = data.get("description")
        self.launchInstructions = data.get("launchInstructions")
        self.type = data.get("type")
        self.behaviour = data.get("behaviour")
        self.tags = data.get("tags")
        self.requirements = data.get("requirements")
        self.logo = data.get("logo")
        self.banner = data.get("banner")
        self.spotlight = data.get("spotlight")
        
    def get_images(self) -> Dict:
        return { "logo": self.logo, "banner": self.banner, "spotlight": self.spotlight }

    def setter(self, data: Dict) -> None:
        self.__dict__.update(data)
    
    def getter(self, attribute) -> None:
        return self.__dict__.get(attribute)