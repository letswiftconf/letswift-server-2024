from pydantic import BaseModel

# Models
class SocialLinks(BaseModel):
    web: str
    email: str
    github: str
    linkedin: str
    x: str
    mastodon: str
    facebook: str
    instagram: str
    thread: str
    youtube: str

class Sponsor(BaseModel):
    id: str
    name: str
    name_en: str
    tier: str
    image_name: str
    image_url: str
    social: SocialLinks

class Organizer(BaseModel):
    id: str
    name: str
    name_en: str
    image_name: str
    image_url: str
    description: str
    social: SocialLinks

class Speaker(BaseModel):
    id: str
    name: str
    name_en: str
    image_name: str
    image_url: str
    description: str
    social: SocialLinks

class Session(BaseModel):
    id: str
    name: str
    name_en: str
    type: str  # opening, ending, event, networking, workshop, presentation, lunch, recess, photo
    track: str
    track_en: str
    venue: str
    venue_en: str
    speaker: Speaker
    start_time: str
    duration: int
    end_time: str
    keynote_url: str
    video_url: str

class FAQ(BaseModel):
    q: str
    a: str
    q_en: str
    a_en: str

class Banner(BaseModel):
    id: str
    image_name: str
    image_url: str
    text: str
    url: str
    is_active: bool