from model import SocialLinks, Sponsor, Organizer, Speaker, Session, FAQ, Banner

# Data
sponsors = [
    Sponsor(
        id="1",
        name="Diamond Sponsor",
        name_en="Diamond Sponsor EN",
        tier="Diamond",
        image_name="diamond.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.diamondsponsor.com",
            email="contact@diamondsponsor.com",
            github="https://github.com/diamondsponsor",
            x="https://x.com/diamondsponsor",
            facebook="https://facebook.com/diamondsponsor",
            instagram="https://instagram.com/diamondsponsor",
            thread="",
            linkedin="https://linkedin.com/diamondsponsor",
            youtube="https://youtube.com/diamondsponsor",
            mastodon="https://mastodon.social/@diamondsponsor"
        )
    ),
    Sponsor(
        id="2",
        name="Gold Sponsor",
        name_en="Gold Sponsor EN",
        tier="Gold",
        image_name="goldsponsor.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.goldsponsor.com",
            email="contact@goldsponsor.com",
            github="https://github.com/goldsponsor",
            x="https://x.com/goldsponsor",
            facebook="https://facebook.com/goldsponsor",
            instagram="https://instagram.com/goldsponsor",
            thread="",
            linkedin="https://linkedin.com/goldsponsor",
            youtube="https://youtube.com/goldsponsor",
            mastodon="https://mastodon.social/@goldsponsor"
        )
    ),
    Sponsor(
        id="3",
        name="Silver Sponsor 1",
        name_en="Silver Sponsor 1 EN",
        tier="Silver",
        image_name="silversponsor1.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.silversponsor1.com",
            email="contact@silversponsor1.com",
            github="https://github.com/silversponsor1",
            x="https://x.com/silversponsor1",
            facebook="https://facebook.com/silversponsor1",
            instagram="https://instagram.com/silversponsor1",
            thread="",
            linkedin="https://linkedin.com/silversponsor1",
            youtube="https://youtube.com/silversponsor1",
            mastodon="https://mastodon.social/@silversponsor1"
        )
    ),
    Sponsor(
        id="4",
        name="Silver Sponsor 2",
        name_en="Silver Sponsor 2 EN",
        tier="Silver",
        image_name="silversponsor2.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.silversponsor2.com",
            email="contact@silversponsor2.com",
            github="https://github.com/silversponsor2",
            x="https://x.com/silversponsor2",
            facebook="https://facebook.com/silversponsor2",
            instagram="https://instagram.com/silversponsor2",
            thread="",
            linkedin="https://linkedin.com/silversponsor2",
            youtube="https://youtube.com/silversponsor2",
            mastodon="https://mastodon.social/@silversponsor2"
        )
    ),
    Sponsor(
        id="5",
        name="Silver Sponsor 3",
        name_en="Silver Sponsor 3 EN",
        tier="Silver",
        image_name="silversponsor3.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.silversponsor3.com",
            email="contact@silversponsor3.com",
            github="https://github.com/silversponsor3",
            x="https://x.com/silversponsor3",
            facebook="https://facebook.com/silversponsor3",
            instagram="https://instagram.com/silversponsor3",
            thread="",
            linkedin="https://linkedin.com/silversponsor3",
            youtube="https://youtube.com/silversponsor3",
            mastodon="https://mastodon.social/@silversponsor3"
        )
    ),
    Sponsor(
        id="6",
        name="Startup Sponsor 1",
        name_en="Startup Sponsor 1 EN",
        tier="Startup",
        image_name="startupsponsor1.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.startupsponsor1.com",
            email="contact@startupsponsor1.com",
            github="https://github.com/startupsponsor1",
            x="https://x.com/startupsponsor1",
            facebook="https://facebook.com/startupsponsor1",
            instagram="https://instagram.com/startupsponsor1",
            thread="",
            linkedin="https://linkedin.com/startupsponsor1",
            youtube="https://youtube.com/startupsponsor1",
            mastodon="https://mastodon.social/@startupsponsor1"
        )
    ),
    Sponsor(
        id="7",
        name="Startup Sponsor 2",
        name_en="Startup Sponsor 2 EN",
        tier="Startup",
        image_name="startupsponsor2.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.startupsponsor2.com",
            email="contact@startupsponsor2.com",
            github="https://github.com/startupsponsor2",
            x="https://x.com/startupsponsor2",
            facebook="https://facebook.com/startupsponsor2",
            instagram="https://instagram.com/startupsponsor2",
            thread="",
            linkedin="https://linkedin.com/startupsponsor2",
            youtube="https://youtube.com/startupsponsor2",
            mastodon="https://mastodon.social/@startupsponsor2"
        )
    ),
    Sponsor(
        id="8",
        name="Startup Sponsor 3",
        name_en="Startup Sponsor 3 EN",
        tier="Startup",
        image_name="startupsponsor3.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.startupsponsor3.com",
            email="contact@startupsponsor3.com",
            github="https://github.com/startupsponsor3",
            x="https://x.com/startupsponsor3",
            facebook="https://facebook.com/startupsponsor3",
            instagram="https://instagram.com/startupsponsor3",
            thread="",
            linkedin="https://linkedin.com/startupsponsor3",
            youtube="https://youtube.com/startupsponsor3",
            mastodon="https://mastodon.social/@startupsponsor3"
        )
    ),
    Sponsor(
        id="9",
        name="Startup Sponsor 4",
        name_en="Startup Sponsor 4 EN",
        tier="Startup",
        image_name="startupsponsor4.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.startupsponsor4.com",
            email="contact@startupsponsor4.com",
            github="https://github.com/startupsponsor4",
            x="https://x.com/startupsponsor4",
            facebook="https://facebook.com/startupsponsor4",
            instagram="https://instagram.com/startupsponsor4",
            thread="",
            linkedin="https://linkedin.com/startupsponsor4",
            youtube="https://youtube.com/startupsponsor4",
            mastodon="https://mastodon.social/@startupsponsor4"
        )
    ),
    Sponsor(
        id="10",
        name="Startup Sponsor 5",
        name_en="Startup Sponsor 5 EN",
        tier="Startup",
        image_name="startupsponsor5.png",
        image_url="https://via.placeholder.com/150",
        social=SocialLinks(
            web="https://www.startupsponsor5.com",
            email="contact@startupsponsor5.com",
            github="https://github.com/startupsponsor5",
            x="https://x.com/startupsponsor5",
            facebook="https://facebook.com/startupsponsor5",
            instagram="https://instagram.com/startupsponsor5",
            thread="",
            linkedin="https://linkedin.com/startupsponsor5",
            youtube="https://youtube.com/startupsponsor5",
            mastodon="https://mastodon.social/@startupsponsor5"
        )
    )
]

organizers = [
    Organizer(
        id="1",
        name="Staff 1",
        name_en="Staff 1 EN",
        image_name="staff1.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 1 description",
        social=SocialLinks(
            web="https://www.staff1.com",
            email="contact@staff1.com",
            github="https://github.com/staff1",
            x="https://x.com/staff1",
            facebook="https://facebook.com/staff1",
            instagram="https://instagram.com/staff1",
            thread="",
            linkedin="https://linkedin.com/staff1",
            youtube="https://youtube.com/staff1",
            mastodon="https://mastodon.social/@staff1"
        )
    ),
    Organizer(
        id="2",
        name="Staff 2",
        name_en="Staff 2 EN",
        image_name="staff2.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 2 description",
        social=SocialLinks(
            web="https://www.staff2.com",
            email="contact@staff2.com",
            github="https://github.com/staff2",
            x="https://x.com/staff2",
            facebook="https://facebook.com/staff2",
            instagram="https://instagram.com/staff2",
            thread="",
            linkedin="https://linkedin.com/staff2",
            youtube="https://youtube.com/staff2",
            mastodon="https://mastodon.social/@staff2"
        )
    ),
    Organizer(
        id="3",
        name="Staff 3",
        name_en="Staff 3 EN",
        image_name="staff3.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 3 description",
        social=SocialLinks(
            web="https://www.staff3.com",
            email="contact@staff3.com",
            github="https://github.com/staff3",
            x="https://x.com/staff3",
            facebook="https://facebook.com/staff3",
            instagram="https://instagram.com/staff3",
            thread="",
            linkedin="https://linkedin.com/staff3",
            youtube="https://youtube.com/staff3",
            mastodon="https://mastodon.social/@staff3"
        )
    ),
    Organizer(
        id="4",
        name="Staff 4",
        name_en="Staff 4 EN",
        image_name="staff4.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 4 description",
        social=SocialLinks(
            web="https://www.staff4.com",
            email="contact@staff4.com",
            github="https://github.com/staff4",
            x="https://x.com/staff4",
            facebook="https://facebook.com/staff4",
            instagram="https://instagram.com/staff4",
            thread="",
            linkedin="https://linkedin.com/staff4",
            youtube="https://youtube.com/staff4",
            mastodon="https://mastodon.social/@staff4"
        )
    ),
    Organizer(
        id="5",
        name="Staff 5",
        name_en="Staff 5 EN",
        image_name="staff5.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 5 description",
        social=SocialLinks(
            web="https://www.staff5.com",
            email="contact@staff5.com",
            github="https://github.com/staff5",
            x="https://x.com/staff5",
            facebook="https://facebook.com/staff5",
            instagram="https://instagram.com/staff5",
            thread="",
            linkedin="https://linkedin.com/staff5",
            youtube="https://youtube.com/staff5",
            mastodon="https://mastodon.social/@staff5"
        )
    ),
    Organizer(
        id="6",
        name="Staff 6",
        name_en="Staff 6 EN",
        image_name="staff6.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 6 description",
        social=SocialLinks(
            web="https://www.staff6.com",
            email="contact@staff6.com",
            github="https://github.com/staff6",
            x="https://x.com/staff6",
            facebook="https://facebook.com/staff6",
            instagram="https://instagram.com/staff6",
            thread="",
            linkedin="https://linkedin.com/staff6",
            youtube="https://youtube.com/staff6",
            mastodon="https://mastodon.social/@staff6"
        )
    ),
    Organizer(
        id="7",
        name="Staff 7",
        name_en="Staff 7 EN",
        image_name="staff7.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 7 description",
        social=SocialLinks(
            web="https://www.staff7.com",
            email="contact@staff7.com",
            github="https://github.com/staff7",
            x="https://x.com/staff7",
            facebook="https://facebook.com/staff7",
            instagram="https://instagram.com/staff7",
            thread="",
            linkedin="https://linkedin.com/staff7",
            youtube="https://youtube.com/staff7",
            mastodon="https://mastodon.social/@staff7"
        )
    ),
    Organizer(
        id="8",
        name="Staff 8",
        name_en="Staff 8 EN",
        image_name="staff8.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 8 description",
        social=SocialLinks(
            web="https://www.staff8.com",
            email="contact@staff8.com",
            github="https://github.com/staff8",
            x="https://x.com/staff8",
            facebook="https://facebook.com/staff8",
            instagram="https://instagram.com/staff8",
            thread="",
            linkedin="https://linkedin.com/staff8",
            youtube="https://youtube.com/staff8",
            mastodon="https://mastodon.social/@staff8"
        )
    ),
    Organizer(
        id="9",
        name="Staff 9",
        name_en="Staff 9 EN",
        image_name="staff9.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 9 description",
        social=SocialLinks(
            web="https://www.staff9.com",
            email="contact@staff9.com",
            github="https://github.com/staff9",
            x="https://x.com/staff9",
            facebook="https://facebook.com/staff9",
            instagram="https://instagram.com/staff9",
            thread="",
            linkedin="https://linkedin.com/staff9",
            youtube="https://youtube.com/staff9",
            mastodon="https://mastodon.social/@staff9"
        )
    ),
    Organizer(
        id="10",
        name="Staff 10",
        name_en="Staff 10 EN",
        image_name="staff10.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 10 description",
        social=SocialLinks(
            web="https://www.staff10.com",
            email="contact@staff10.com",
            github="https://github.com/staff10",
            x="https://x.com/staff10",
            facebook="https://facebook.com/staff10",
            instagram="https://instagram.com/staff10",
            thread="",
            linkedin="https://linkedin.com/staff10",
            youtube="https://youtube.com/staff10",
            mastodon="https://mastodon.social/@staff10"
        )
    ),
    Organizer(
        id="11",
        name="Staff 11",
        name_en="Staff 11 EN",
        image_name="staff11.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 11 description",
        social=SocialLinks(
            web="https://www.staff11.com",
            email="contact@staff11.com",
            github="https://github.com/staff11",
            x="https://x.com/staff11",
            facebook="https://facebook.com/staff11",
            instagram="https://instagram.com/staff11",
            thread="",
            linkedin="https://linkedin.com/staff11",
            youtube="https://youtube.com/staff11",
            mastodon="https://mastodon.social/@staff11"
        )
    ),
    Organizer(
        id="12",
        name="Staff 12",
        name_en="Staff 12 EN",
        image_name="staff12.png",
        image_url="https://via.placeholder.com/150",
        description="Staff 12 description",
        social=SocialLinks(
            web="https://www.staff12.com",
            email="contact@staff12.com",
            github="https://github.com/staff12",
            x="https://x.com/staff12",
            facebook="https://facebook.com/staff12",
            instagram="https://instagram.com/staff12",
            thread="",
            linkedin="https://linkedin.com/staff12",
            youtube="https://youtube.com/staff12",
            mastodon="https://mastodon.social/@staff12"
        )
    )
]

speakers = [
    Speaker(
        id="1",
        name="Speaker 1",
        name_en="Speaker 1 EN",
        image_name="speaker1.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 1 bio",
        social=SocialLinks(
            web="https://www.speaker1.com",
            email="contact@speaker1.com",
            github="https://github.com/speaker1",
            x="https://x.com/speaker1",
            facebook="https://facebook.com/speaker1",
            instagram="https://instagram.com/speaker1",
            thread="",
            linkedin="https://linkedin.com/speaker1",
            youtube="https://youtube.com/speaker1",
            mastodon="https://mastodon.social/@speaker1"
        )
    ),
    Speaker(
        id="2",
        name="Speaker 2",
        name_en="Speaker 2 EN",
        image_name="speaker2.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 2 bio",
        social=SocialLinks(
            web="https://www.speaker2.com",
            email="contact@speaker2.com",
            github="https://github.com/speaker2",
            x="https://x.com/speaker2",
            facebook="https://facebook.com/speaker2",
            instagram="https://instagram.com/speaker2",
            thread="",
            linkedin="https://linkedin.com/speaker2",
            youtube="https://youtube.com/speaker2",
            mastodon="https://mastodon.social/@speaker2"
        )
    ),
    Speaker(
        id="3",
        name="Speaker 3",
        name_en="Speaker 3 EN",
        image_name="speaker3.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 3 bio",
        social=SocialLinks(
            web="https://www.speaker3.com",
            email="contact@speaker3.com",
            github="https://github.com/speaker3",
            x="https://x.com/speaker3",
            facebook="https://facebook.com/speaker3",
            instagram="https://instagram.com/speaker3",
            thread="",
            linkedin="https://linkedin.com/speaker3",
            youtube="https://youtube.com/speaker3",
            mastodon="https://mastodon.social/@speaker3"
        )
    ),
    Speaker(
        id="4",
        name="Speaker 4",
        name_en="Speaker 4 EN",
        image_name="speaker4.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 4 bio",
        social=SocialLinks(
            web="https://www.speaker4.com",
            email="contact@speaker4.com",
            github="https://github.com/speaker4",
            x="https://x.com/speaker4",
            facebook="https://facebook.com/speaker4",
            instagram="https://instagram.com/speaker4",
            thread="",
            linkedin="https://linkedin.com/speaker4",
            youtube="https://youtube.com/speaker4",
            mastodon="https://mastodon.social/@speaker4"
        )
    ),
    Speaker(
        id="5",
        name="Speaker 5",
        name_en="Speaker 5 EN",
        image_name="speaker5.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 5 bio",
        social=SocialLinks(
            web="https://www.speaker5.com",
            email="contact@speaker5.com",
            github="https://github.com/speaker5",
            x="https://x.com/speaker5",
            facebook="https://facebook.com/speaker5",
            instagram="https://instagram.com/speaker5",
            thread="",
            linkedin="https://linkedin.com/speaker5",
            youtube="https://youtube.com/speaker5",
            mastodon="https://mastodon.social/@speaker5"
        )
    ),
    Speaker(
        id="6",
        name="Speaker 6",
        name_en="Speaker 6 EN",
        image_name="speaker6.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 6 bio",
        social=SocialLinks(
            web="https://www.speaker6.com",
            email="contact@speaker6.com",
            github="https://github.com/speaker6",
            x="https://x.com/speaker6",
            facebook="https://facebook.com/speaker6",
            instagram="https://instagram.com/speaker6",
            thread="",
            linkedin="https://linkedin.com/speaker6",
            youtube="https://youtube.com/speaker6",
            mastodon="https://mastodon.social/@speaker6"
        )
    ),
    Speaker(
        id="7",
        name="Speaker 7",
        name_en="Speaker 7 EN",
        image_name="speaker7.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 7 bio",
        social=SocialLinks(
            web="https://www.speaker7.com",
            email="contact@speaker7.com",
            github="https://github.com/speaker7",
            x="https://x.com/speaker7",
            facebook="https://facebook.com/speaker7",
            instagram="https://instagram.com/speaker7",
            thread="",
            linkedin="https://linkedin.com/speaker7",
            youtube="https://youtube.com/speaker7",
            mastodon="https://mastodon.social/@speaker7"
        )
    ),
    Speaker(
        id="8",
        name="Speaker 8",
        name_en="Speaker 8 EN",
        image_name="speaker8.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 8 bio",
        social=SocialLinks(
            web="https://www.speaker8.com",
            email="contact@speaker8.com",
            github="https://github.com/speaker8",
            x="https://x.com/speaker8",
            facebook="https://facebook.com/speaker8",
            instagram="https://instagram.com/speaker8",
            thread="",
            linkedin="https://linkedin.com/speaker8",
            youtube="https://youtube.com/speaker8",
            mastodon="https://mastodon.social/@speaker8"
        )
    ),
    Speaker(
        id="9",
        name="Speaker 9",
        name_en="Speaker 9 EN",
        image_name="speaker9.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 9 bio",
        social=SocialLinks(
            web="https://www.speaker9.com",
            email="contact@speaker9.com",
            github="https://github.com/speaker9",
            x="https://x.com/speaker9",
            facebook="https://facebook.com/speaker9",
            instagram="https://instagram.com/speaker9",
            thread="",
            linkedin="https://linkedin.com/speaker9",
            youtube="https://youtube.com/speaker9",
            mastodon="https://mastodon.social/@speaker9"
        )
    ),
    Speaker(
        id="10",
        name="Speaker 10",
        name_en="Speaker 10 EN",
        image_name="speaker10.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 10 bio",
        social=SocialLinks(
            web="https://www.speaker10.com",
            email="contact@speaker10.com",
            github="https://github.com/speaker10",
            x="https://x.com/speaker10",
            facebook="https://facebook.com/speaker10",
            instagram="https://instagram.com/speaker10",
            thread="",
            linkedin="https://linkedin.com/speaker10",
            youtube="https://youtube.com/speaker10",
            mastodon="https://mastodon.social/@speaker10"
        )
    ),
    Speaker(
        id="11",
        name="Speaker 11",
        name_en="Speaker 11 EN",
        image_name="speaker11.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 11 bio",
        social=SocialLinks(
            web="https://www.speaker11.com",
            email="contact@speaker11.com",
            github="https://github.com/speaker11",
            x="https://x.com/speaker11",
            facebook="https://facebook.com/speaker11",
            instagram="https://instagram.com/speaker11",
            thread="",
            linkedin="https://linkedin.com/speaker11",
            youtube="https://youtube.com/speaker11",
            mastodon="https://mastodon.social/@speaker11"
        )
    ),
    Speaker(
        id="12",
        name="Speaker 12",
        name_en="Speaker 12 EN",
        image_name="speaker12.png",
        image_url="https://via.placeholder.com/150",
        description="Speaker 12 bio",
        social=SocialLinks(
            web="https://www.speaker12.com",
            email="contact@speaker12.com",
            github="https://github.com/speaker12",
            x="https://x.com/speaker12",
            facebook="https://facebook.com/speaker12",
            instagram="https://instagram.com/speaker12",
            thread="",
            linkedin="https://linkedin.com/speaker12",
            youtube="https://youtube.com/speaker12",
            mastodon="https://mastodon.social/@speaker12"
        )
    )
]

sessions = [
    Session(
        id="1",
        name="Session 1",
        name_en="Session 1 EN",
        type="presentation",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[0],
        start_time="2024-08-01T09:00:00",
        duration=3600,
        end_time="2024-08-01T10:00:00",
        keynote_url="https://www.keynote1.com",
        video_url="https://www.video1.com"
    ),
    Session(
        id="2",
        name="Session 2: Exploring New Technologies",
        name_en="Session 2 EN: Exploring New Technologies",
        type="workshop",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[1],
        start_time="2024-08-01T10:00:00",
        duration=3600,
        end_time="2024-08-01T11:00:00",
        keynote_url="https://www.keynote2.com",
        video_url="https://www.video2.com"
    ),
    Session(
        id="3",
        name="Session 3: Future of AI",
        name_en="Session 3 EN: Future of AI",
        type="panel",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[2],
        start_time="2024-08-01T11:00:00",
        duration=3600,
        end_time="2024-08-01T12:00:00",
        keynote_url="https://www.keynote3.com",
        video_url="https://www.video3.com"
    ),
    Session(
        id="4",
        name="Session 4: Deep Dive into Machine Learning",
        name_en="Session 4 EN: Deep Dive into Machine Learning",
        type="presentation",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[3],
        start_time="2024-08-01T12:00:00",
        duration=3600,
        end_time="2024-08-01T13:00:00",
        keynote_url="https://www.keynote4.com",
        video_url="https://www.video4.com"
    ),
    Session(
        id="5",
        name="Session 5: Innovations in Cloud Computing",
        name_en="Session 5 EN: Innovations in Cloud Computing",
        type="workshop",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[4],
        start_time="2024-08-01T13:00:00",
        duration=3600,
        end_time="2024-08-01T14:00:00",
        keynote_url="https://www.keynote5.com",
        video_url="https://www.video5.com"
    ),
    Session(
        id="6",
        name="Session 6: The Rise of Quantum Computing",
        name_en="Session 6 EN: The Rise of Quantum Computing",
        type="presentation",
        track="Track A",
        track_en="Track A EN",
        venue="Main Hall",
        venue_en="Main Hall EN",
        speaker=speakers[5],
        start_time="2024-08-01T14:00:00",
        duration=3600,
        end_time="2024-08-01T15:00:00",
        keynote_url="https://www.keynote6.com",
        video_url="https://www.video6.com"
    ),
    Session(
        id="7",
        name="Session 7: Understanding Blockchain",
        name_en="Session 7 EN: Understanding Blockchain",
        type="panel",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[6],
        start_time="2024-08-01T09:00:00",
        duration=3600,
        end_time="2024-08-01T10:00:00",
        keynote_url="https://www.keynote7.com",
        video_url="https://www.video7.com"
    ),
    Session(
        id="8",
        name="Session 8: Advances in Data Privacy",
        name_en="Session 8 EN: Advances in Data Privacy",
        type="workshop",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[7],
        start_time="2024-08-01T10:00:00",
        duration=3600,
        end_time="2024-08-01T11:00:00",
        keynote_url="https://www.keynote8.com",
        video_url="https://www.video8.com"
    ),
    Session(
        id="9",
        name="Session 9: Cybersecurity in 2024",
        name_en="Session 9 EN: Cybersecurity in 2024",
        type="presentation",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[8],
        start_time="2024-08-01T11:00:00",
        duration=3600,
        end_time="2024-08-01T12:00:00",
        keynote_url="https://www.keynote9.com",
        video_url="https://www.video9.com"
    ),
    Session(
        id="10",
        name="Session 10: The Evolution of UX Design",
        name_en="Session 10 EN: The Evolution of UX Design",
        type="panel",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[9],
        start_time="2024-08-01T12:00:00",
        duration=3600,
        end_time="2024-08-01T13:00:00",
        keynote_url="https://www.keynote10.com",
        video_url="https://www.video10.com"
    ),
    Session(
        id="11",
        name="Session 11: The Impact of AI on Everyday Life",
        name_en="Session 11 EN: The Impact of AI on Everyday Life",
        type="workshop",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[10],
        start_time="2024-08-01T13:00:00",
        duration=3600,
        end_time="2024-08-01T14:00:00",
        keynote_url="https://www.keynote11.com",
        video_url="https://www.video11.com"
    ),
    Session(
        id="12",
        name="Session 12: Future Trends in Web Development",
        name_en="Session 12 EN: Future Trends in Web Development",
        type="presentation",
        track="Track A",
        track_en="Track A EN",
        venue="Breakout Room",
        venue_en="Breakout Room EN",
        speaker=speakers[11],
        start_time="2024-08-01T14:00:00",
        duration=3600,
        end_time="2024-08-01T15:00:00",
        keynote_url="https://www.keynote12.com",
        video_url="https://www.video12.com"
    )
]

faqs = [
    FAQ(
        q="What is the purpose of this event?",
        a="This event aims to bring together industry leaders and enthusiasts to discuss the latest trends and advancements in technology. We hope to provide valuable insights and networking opportunities for all participants.",
        q_en="What is the purpose of this event EN?",
        a_en="This event aims to bring together industry leaders and enthusiasts to discuss the latest trends and advancements in technology. We hope to provide valuable insights and networking opportunities for all participants EN."
    ),
    FAQ(
        q="How can I register for the conference?",
        a="To register for the conference, please visit our website and fill out the registration form. You can choose your preferred sessions and pay the registration fee online. Ensure you complete all required fields before submitting your application.",
        q_en="How can I register for the conference EN?",
        a_en="To register for the conference, please visit our website and fill out the registration form. You can choose your preferred sessions and pay the registration fee online. Ensure you complete all required fields before submitting your application EN."
    ),
    FAQ(
        q="What is the schedule for the sessions?",
        a="The schedule for the sessions can be found on our event website under the 'Agenda' section. We have multiple tracks running concurrently, so please review the schedule carefully to plan your day effectively. Each session has a specified start and end time.",
        q_en="What is the schedule for the sessions EN?",
        a_en="The schedule for the sessions can be found on our event website under the 'Agenda' section. We have multiple tracks running concurrently, so please review the schedule carefully to plan your day effectively EN."
    ),
    FAQ(
        q="Will there be any virtual sessions available?",
        a="Yes, we will offer virtual sessions for those who cannot attend in person. These sessions will be streamed live and will also be available on-demand after the event. Make sure to check our website for more details on accessing the virtual content.",
        q_en="Will there be any virtual sessions available EN?",
        a_en="Yes, we will offer virtual sessions for those who cannot attend in person. These sessions will be streamed live and will also be available on-demand after the event EN."
    ),
    FAQ(
        q="Can I update my registration details after submission?",
        a="Yes, you can update your registration details by logging into your account on our website. If you encounter any issues or need further assistance, please contact our support team at support@example.com.",
        q_en="Can I update my registration details after submission EN?",
        a_en="Yes, you can update your registration details by logging into your account on our website. If you encounter any issues or need further assistance, please contact our support team at support@example.com EN."
    ),
    FAQ(
        q="What should I bring to the event?",
        a="Please bring a valid ID, your event ticket (printed or digital), and any necessary materials for the sessions you plan to attend. If you have any dietary restrictions or special needs, please inform us in advance.",
        q_en="What should I bring to the event EN?",
        a_en="Please bring a valid ID, your event ticket (printed or digital), and any necessary materials for the sessions you plan to attend EN."
    ),
    FAQ(
        q="Are there any discounts available for early registration?",
        a="Yes, we offer early bird discounts for those who register before the specified deadline. The discount rates and deadlines are listed on our registration page. Be sure to register early to take advantage of these savings.",
        q_en="Are there any discounts available for early registration EN?",
        a_en="Yes, we offer early bird discounts for those who register before the specified deadline EN."
    ),
    FAQ(
        q="What are the options for accommodation?",
        a="We have partnered with several hotels near the event venue to offer special rates for attendees. A list of recommended hotels is available on our website under the 'Accommodation' section. We encourage you to book early as rooms fill up quickly.",
        q_en="What are the options for accommodation EN?",
        a_en="We have partnered with several hotels near the event venue to offer special rates for attendees EN."
    ),
    FAQ(
        q="Will there be food and beverages provided at the event?",
        a="Yes, we will provide breakfast, lunch, and refreshments throughout the day. Special dietary options will be available. Please inform us of any specific dietary needs in advance so we can accommodate them.",
        q_en="Will there be food and beverages provided at the event EN?",
        a_en="Yes, we will provide breakfast, lunch, and refreshments throughout the day EN."
    ),
    FAQ(
        q="How do I contact the event organizers?",
        a="You can contact the event organizers via email at organizers@example.com or through the contact form on our website. For urgent inquiries, please call our support line at (123) 456-7890.",
        q_en="How do I contact the event organizers EN?",
        a_en="You can contact the event organizers via email at organizers@example.com or through the contact form on our website EN."
    ),
    FAQ(
        q="What is the cancellation policy?",
        a="If you need to cancel your registration, please refer to our cancellation policy on the website. Generally, cancellations made before the deadline will receive a full refund, while those made after may incur a fee. Check the policy for specific details.",
        q_en="What is the cancellation policy EN?",
        a_en="If you need to cancel your registration, please refer to our cancellation policy on the website EN."
    )
]

banners = [
    Banner(
        id="1",
        image_name="banner1.png",
        image_url="https://via.placeholder.com/150",
        text="Banner 1 description",
        url="https://www.banner1.com",
        is_active=True
    ),
]