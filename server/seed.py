#!/usr/bin/env python3

# Standard library imports
from random import randint as ri, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app

from config import db
from models import User, Edit, Page

if __name__ == "__main__":
     fake = Faker()
     with app.app_context():
        print("Starting seed...")
        # clear database
        User.query.delete()
        Edit.query.delete()
        Page.query.delete()
        print("Datebase Cleared")
        marc = User(username="marc123", password_hash="123456")
        yu = User(username="yu1234", password_hash="abcdef")
        tj = User(username="tj1234", password_hash="qweasd")

        db.session.add_all(
            [marc, yu, tj]
        )
        db.session.commit()
        print("Adding users")
        print("Adding pages")
        page_list = []
        page1 = Page(title="Wiccan Symbols", author="yu1234", text=\
"""<h3>Unveiling the Mysteries: A Guide to Wiccan Symbols</h3>
<p>In the realm of spirituality, Wicca stands as a modern pagan, nature-based religion that draws upon ancient traditions, folklore, and magical practices. Central to Wiccan beliefs is a profound connection with nature, the worship of deity and divinity as immanent forces, and the use of rituals and symbols to channel energies for various purposes. Wiccan symbols play a crucial role in embodying and transmitting these beliefs, carrying with them deep meanings and representations that resonate with practitioners. In this article, we delve into the enchanting world of Wiccan symbols, exploring their significance, origins, and the magic they invoke.</p>

<h3>The Pentacle: A Gateway to the Mystical</h3>
<p>One of the most recognizable Wiccan symbols is the pentacle. Typically depicted as a five-pointed star enclosed within a circle, the pentacle is a potent emblem representing the five elements: earth, air, fire, water, and spirit. Each point of the star corresponds to one of these elements, and the circle symbolizes unity, wholeness, and the eternal cycle of life.</p>
<p>Contrary to some misconceptions, the pentacle is not a representation of evil or malevolence. Rather, it embodies the harmonious interplay of natural forces, highlighting Wiccan reverence for the interconnectedness of all things. Wiccans often use the pentacle in rituals and ceremonies to invoke elemental energies, protection, and to focus their intentions.</p>

<h3>The Triquetra: Weaving the Triple Aspects</h3>
<p>Another prominent Wiccan symbol is the triquetra, also known as the triple goddess symbol. This intricate design consists of three interlocked loops, often used to depict the maiden, mother, and crone - the three phases of the goddess and stages of life: youth, maturity, and wisdom. This symbol encapsulates the cyclical nature of existence, the changing seasons, and the perpetual journey of birth, growth, and transformation.</p>
<p>The triquetra also represents the unity of the three realms: land, sea, and sky. Moreover, it mirrors the Wiccan concept of the triple aspect, which is present not only in the goddess but also in the god, emphasizing duality, balance, and the ebb and flow of energy.</p>

<h3>The Crescent Moon: Embracing Mystery and Magic</h3>
<p>Wicca holds a profound reverence for the moon, considering it a source of inspiration, energy, and magic. The crescent moon, with its curving shape, is an emblem of the waxing and waning phases of the moon. It symbolizes renewal, regeneration, and the cycles of life. Additionally, it represents the goddess in her maiden aspect and the energies associated with intuition, dreams, and the subconscious mind.</p>
<p>Wiccans often align their rituals with the phases of the moon, utilizing its energy for spellwork, meditation, and divination. The crescent moon symbolizes their connection with the mystical and their dedication to harnessing the moon's power for spiritual growth.</p>

<h3>The Cauldron: A Vessel of Transformation</h3>
<p>Central to magical practices, the cauldron is a symbol of transformation, rebirth, and the cyclical nature of life. In Wiccan symbolism, the cauldron represents the goddess's womb, a vessel of creation and sustenance. It is often used in rituals for brewing potions, scrying, and transformational spellwork</p>.
<p>The cauldron is also linked to the element of water, symbolizing emotions, intuition, and the subconscious. Through the cauldron's representation, Wiccans embrace the idea that like ingredients in a pot, their experiences blend together to shape their spiritual journey and personal evolution.</p>

<h3>Final Thoughts</h3>
<p>Wiccan symbols serve as bridges between the material and spiritual realms, encapsulating profound beliefs and energies in beautifully intricate forms. Each symbol is a window into Wicca's reverence for nature, balance, and the interconnectedness of all things. From the pentacle's elemental harmony to the triquetra's triple goddess representation, the crescent moon's mystical allure, and the cauldron's transformative power, these symbols guide practitioners on their path of spiritual exploration, magic, and self-discovery.</p>
""")



        page2 = Page(title="Magic Wands", author="tj1234", text=\
"""<h3>Unveiling the Enchantment: The Allure and Mystique of Magic Wands</h3>
<p>In the realm of fantasy and folklore, few objects capture the imagination as vividly as the magic wand. These enchanting tools have been an integral part of countless tales, serving as conduits for wizards, witches, and sorcerers to channel their mystical powers. From the classic stories of Merlin and Gandalf to the modern interpretations in books and movies, the magic wand remains an iconic symbol of the supernatural. In this article, we delve into the fascinating world of magic wands, exploring their origins, significance, and enduring allure.</p>

<h3>Origins and Evolution</h3>
<p>The concept of using a wand-like object to wield magical powers has ancient roots, spanning various cultures and civilizations. Ancient Egyptian priests used staffs and rods to perform rituals and cast spells, while in European history, the wand has been associated with symbols of authority and mysticism. It wasn't until the Middle Ages that the wand began to truly take on its magical connotations.</p>
<p>Throughout history, the portrayal and functionality of magic wands have evolved. In early literature, such as Arthurian legends and medieval romances, wands were often depicted as staves or staffs, emphasizing their connection to wisdom and authority. Over time, the wand transformed into a more refined and delicate instrument, often adorned with precious materials and intricate designs.</p>

<h3>Symbolism and Functionality</h3>
<p>The magic wand's symbolism goes beyond its physical form. It represents the extension of a spellcaster's willpower and intention, allowing them to focus their magical abilities with precision. The act of waving or pointing a wand is a gesture that bridges the gap between the mundane and the supernatural, facilitating the flow of mystical energies.</p>
<p>Wands are often associated with specific magical elements or forces, such as fire, water, earth, and air. In some traditions, they are crafted from materials that align with these elements, further enhancing their potency. For instance, a wand made from oak might be linked to strength and protection, while a willow wand could be associated with intuition and healing.</p>

<h3>Cultural Variations</h3>
<p>Different cultures have their own interpretations of magic wands. In Celtic mythology, the druids used oak wands to access their mystical abilities, while in Native American traditions, shamans employed ceremonial staffs for healing and communication with the spirit world. The concept of a magic wand is also prevalent in Eastern cultures, where Taoist and Buddhist monks utilize ritual implements to channel energy and perform blessings.</p>

<h3>Literary and Pop Culture Influence</h3>
<p>The magic wand's prominence in literature and pop culture is undeniable. It has appeared in numerous iconic works of fiction, often shaping the narrative and the characters within. J.K. Rowling's "Harry Potter" series introduced the world to the concept of wands as essential tools for spellcasting, each with its own unique core and characteristics. This innovation added a layer of complexity to the magic system and gave readers a tangible connection to the wizarding world.</p>
<p>Beyond literature, magic wands have become fixtures in movies, television shows, and video games. From Disney's fairy godmothers to the mystical staff of the sorcerer Mickey Mouse, wands continue to capture the imagination of audiences young and old.</p>

<h3>The Allure of Possibility</h3>
<p>The enduring appeal of magic wands lies in their representation of untapped potential and the unknown. They are instruments of transformation, capable of turning a mere mortal into a formidable spellcaster. Wands evoke a sense of wonder and escapism, inviting us to believe in the extraordinary and embrace the idea that there is more to the world than meets the eye.</p>
<p>Whether you envision yourself as a wizard, a witch, or simply an adventurer in a fantastical realm, the magic wand serves as a reminder that our imagination knows no bounds. As long as tales of enchantment and mystery continue to captivate us, the magic wand will remain an enduring symbol of the magical possibilities that lie just beyond our reach.</p>
""")

        page3 = Page(title="Wiccan Seasons", author="yu1234", text =\
"""<h3>Wiccan Perspectives on the Seasons</h3>
<p>Wicca, a modern pagan, witchcraft religion, is deeply connected to nature and its cycles. The changing of seasons holds significant spiritual importance within the Wiccan tradition.</p>

<h3>Spring Equinox: Ostara</h3>
<p>The Spring Equinox, known as Ostara in Wiccan circles, marks the balance between day and night. Wiccans celebrate the awakening of the earth and the renewal of life. It's a time to honor fertility, growth, and new beginnings. Traditionally, colored eggs and symbols of hares are common during this celebration.</p>
    
<h3>Summer Solstice: Litha</h3>
<p>Litha, the Summer Solstice, is the longest day of the year. Wiccans gather to celebrate the power of the sun and the abundance of the earth. Bonfires, outdoor rituals, and feasting are common during this time. It's a period to embrace the energy of the sun and harness it for personal growth and transformation.</p>
    
<h3>Autumn Equinox: Mabon</h3>
<p>Mabon, the Autumn Equinox, is a time of gratitude and reflection. Wiccans give thanks for the harvest, both physical and spiritual. It's an opportunity to find balance within oneself as the days grow shorter. The changing colors of leaves are often incorporated into rituals, symbolizing the beauty and impermanence of life.</p>
    
<h3>Winter Solstice: Yule</h3>
<p>Yule, the Winter Solstice, marks the rebirth of the sun. It's a celebration of light and hope during the darkest time of the year. Wiccans exchange gifts, light candles, and decorate evergreen trees. Yule emphasizes the cyclical nature of life, reminding practitioners that even in darkness, light will return.</p>
    
<h3>Connecting with the Seasons</h3>
<p>Wiccans often celebrate these seasonal festivals through rituals, spells, and gatherings. They align their spiritual practices with the natural world, using the energy of each season to enhance their magical workings and personal growth.</p>

<h3>Conclusion</h3>
<p>For Wiccans, the seasons are more than just changes in weather; they represent deeper cycles of life, death, and rebirth. Through their connection to nature, Wiccans find meaning, inspiration, and a sense of unity with the universe.</p>
""")

        page4 = Page(title="Potion Making", author="marc123", text=\
"""<p>Creating potions is a sacred and time-honored practice in the realm of witchcraft. These concoctions hold the power to heal, protect, and enhance various aspects of our lives. Whether you're a seasoned witch or just starting on your magical journey, potion making can be a fulfilling and magical experience.</p>

<h3>Ingredients and Tools</h3>
<p>The key to successful potion making lies in the selection of the right ingredients and tools. Herbs, crystals, essential oils, and other magical elements are often used to infuse potions with their intended properties. A mortar and pestle, cauldron, and various vials are essential tools for brewing your mixtures.</p>

<h3>Setting Your Intention</h3>
<p>Before you begin, it's important to set a clear intention for your potion. Decide what purpose your potion will serve – whether it's for love, protection, clarity, or any other desired outcome. Your intention will guide your energy and focus throughout the potion-making process.</p>

<h3>Creating the Potion</h3>
<p>Begin by gathering your chosen ingredients and placing them on your workspace. As you add each ingredient to your cauldron or mixing vessel, visualize your intention and the energy you wish to infuse into the potion. Stir the mixture clockwise to attract the intended energy and counterclockwise to banish negativity.</p>

<h3>Infusing Magic</h3>
<p>Infuse your potion with magic by reciting incantations, invocations, or affirmations that align with your intention. Feel the energy of the ingredients and your intention coming together as you speak your words of power. This step deepens the potency of your potion.</p>

<h3>Charging and Storing</h3>
<p>Once your potion is brewed, it's time to charge it with energy. Place it in a spot where it can be exposed to moonlight, sunlight, or other sources of natural energy for a specific duration. After charging, store your potion in glass vials or bottles to preserve its magical properties.</p>

<h3>Safe Practices</h3>
<p>While potion making can be a beautiful and transformative practice, it's essential to prioritize safety. Some herbs and substances can be toxic or cause adverse reactions. Always research the properties of your chosen ingredients and use caution when handling them.</p>

<h3>Conclusion</h3>
<p>Potion making is a profound way to connect with the energies of nature and manifest your desires through magical means. Whether you're crafting potions for personal use or to share with others, remember that your intentions and energy are the most potent ingredients. With practice, patience, and respect for the craft, potion making can become a cherished aspect of your magical journey.</p>
""")

        page5 = Page(title="Wiccan Rituals", author="marc123", text=\
"""<h3>Wiccan Rituals</h3>
<p>Wicca, a modern pagan, witchcraft religion, places a strong emphasis on connecting with nature and the divine through rituals. These rituals are not only a means of spiritual expression but also a way to honor the cycles of nature, celebrate life events, and foster a deeper connection with the self and the universe.</p>

<h3>The Wheel of the Year</h3>
<p>Central to Wiccan rituals is the celebration of the Wheel of the Year, which consists of eight Sabbats that mark the changing seasons. These Sabbats are divided into two groups: the solar festivals, or the solstices and equinoxes, and the cross-quarter festivals, which fall between the solstices and equinoxes.</p>

<h3>Full Moon and New Moon Rituals</h3>
<p>Wiccans also place significance on lunar cycles, particularly the full moon and new moon. Full moon rituals are often associated with releasing negativity, setting intentions, and tapping into heightened energy. New moon rituals, on the other hand, are about new beginnings, setting goals, and planting seeds for personal growth.</p>

<h3>Elements and Altar Setup</h3>
<p>Wiccan rituals commonly involve the four classical elements  "Earth, Air, Fire, and Water" each representing different aspects of life and nature. Practitioners often set up altars with representations of these elements, along with other symbolic items like candles, crystals, herbs, and tools such as athames and chalices.</p>

<h3>Casting Circles and Invoking Deities</h3>
<p>Before performing rituals, Wiccans typically cast a sacred circle to create a protected space where magical work can take place. Deities, often associated with nature, fertility, and magic, are invoked to lend their guidance and energy to the ritual. These deities can vary based on the practitioner's personal pantheon or belief system.</p>

<h3>Spellwork and Intention Setting</h3>
<p>Wiccan rituals often include spellwork, which involves using focused intent, visualization, and energy to manifest desired outcomes. Spells can range from simple affirmations to more elaborate rituals involving herbs, candles, and other tools. The intention behind the spell is key, as it aligns the practitioner's energy with their desired goal.</p>

<h3>Harvest Festivals and Celebrations</h3>
<p>Harvest festivals, such as Lammas (Lughnasadh) and Mabon, hold a special place in Wiccan practices. These festivals celebrate the fruits of the Earth's labor and express gratitude for the abundance provided by nature. They are a time of reflection, sharing, and feasting with the Wiccan community.</p>

<h3>Conclusion</h3>
<p>Wiccan rituals are a beautiful blend of spirituality, nature reverence, and personal empowerment. Through these practices, Wiccans seek to connect with the energies of the natural world, foster personal growth, and create positive changes in their lives. The diversity of rituals within Wicca allows for individual expression while staying rooted in the shared values of harmony, balance, and respect for all living beings.</p>
""")

        page6=Page(title='Hocus Pocus', author="tj1234", text=\
"""<h3>Unraveling the Magic of "Hocus Pocus": A Timeless Tale of Enchantment and Halloween</h3>
<p>Every year, as the leaves turn shades of gold and the air becomes crisper, the enchanting aroma of pumpkin spice and the distant echo of cackles signal the approach of Halloween. And at the heart of this bewitching season lies a beloved cinematic gem that has become a timeless tradition for many: "Hocus Pocus." This spellbinding film weaves together humor, magic, and a touch of nostalgia, creating a bewitching concoction that has charmed audiences for nearly three decades.</p>

<h3>A Spellbinding Story</h3>
<p>Released in 1993 and directed by Kenny Ortega, "Hocus Pocus" tells the tale of three witch sisters—Winifred, Sarah, and Mary Sanderson—who are resurrected in modern-day Salem, Massachusetts, 300 years after their initial demise. Thirsting for eternal life, the witches embark on a quest to regain their youth by sucking the life force from children. The plot thickens as a trio of unlikely heroes, Max Dennison, his sister Dani, and their newfound friend Allison, attempt to thwart the witches' nefarious plans.</p>
<p>The film's whimsical narrative is brimming with humorous mishaps and magical mayhem. The bumbling yet endearing Sanderson sisters stumble through a world they hardly recognize, giving rise to comedic situations that are sure to elicit laughter from audiences of all ages. The blend of supernatural elements and witty dialogue creates a captivating experience that perfectly captures the spirit of Halloween.</p>

<h3>A Charismatic Coven</h3>
<p>Central to the film's allure is the trio of witches portrayed by Bette Midler (Winifred), Sarah Jessica Parker (Sarah), and Kathy Najimy (Mary). Each actress delivers a stellar performance that not only embraces their characters' wickedness but also infuses them with an undeniable charisma. Bette Midler's commanding presence as the cunning Winifred Sanderson, in particular, has become iconic, with her fiery red hair and penchant for delivering delightfully sinister lines.</p>
<p>The chemistry between the Sanderson sisters is palpable, adding depth to their characters and making their interactions all the more entertaining. Their over-the-top antics, unique personalities, and hilarious one-liners have transformed them into beloved figures in popular culture.</p>

<h3>A Nostalgic Brew</h3>
<p>"Hocus Pocus" has achieved cult status largely due to its ability to evoke feelings of nostalgia. For many, the film is a cherished part of their childhood Halloween memories. The blend of supernatural fantasy, teenage romance, and coming-of-age themes appeals to a wide audience, allowing both young and old to find something to enjoy within its magical universe.</p>
<p>The film's soundtrack, featuring songs like "I Put a Spell on You," adds an extra layer of enchantment. The annual resurgence of these musical numbers during the Halloween season has become a tradition in itself, rekindling the enchanting spirit of the film year after year.</p>

<h3>A Timeless Tradition</h3>
<p>As the years have passed, "Hocus Pocus" has continued to capture the hearts of new generations. Its annual airing on television and availability on streaming platforms has ensured its enduring popularity. The film's fan base has grown to include those who remember its initial release as well as younger audiences who are discovering its magic for the first time.</p>
<p>Beyond the screen, "Hocus Pocus" has inspired countless Halloween costumes, fan art, and even stage adaptations. The Sanderson sisters' image has become synonymous with the holiday, creating a sense of connection across different generations and communities.</p>
<p>In an ever-changing world, the timeless tale of "Hocus Pocus" continues to remind us of the magic that can be found in the most unexpected places. Its ability to bring joy, laughter, and a touch of the supernatural into our lives is a testament to the enduring power of storytelling.</p>

<h3>Conclusion: A Spell That Endures</h3>
<p>"Hocus Pocus" is more than just a film; it's a bewitching experience that has woven its way into the fabric of Halloween traditions. With its captivating story, memorable characters, and nostalgic charm, the movie has cast a spell on audiences that shows no sign of breaking. As the Sanderson sisters' misadventures continue to enchant both young and old, "Hocus Pocus" remains a timeless testament to the magic of cinema and the enduring allure of the Halloween season.</p>
""")

        page7 = Page(title="Vampires vs. Witches: Unraveling the Mystical Showdown", author="yu1234", text=\
"""<p>Throughout history, the realms of myth and legend have been populated by a diverse cast of supernatural beings, each with its own set of powers, lore, and allure. Among these enigmatic entities, two figures stand out as perennial favorites in the annals of folklore: vampires and witches. These two distinct yet interconnected archetypes have captivated the human imagination for centuries, inspiring tales of dark romance, trepidation, and magical intrigue. In this article, we delve into the captivating clash between vampires and witches, exploring their origins, characteristics, and the allure they hold over our collective psyche.</p>

<h3>The Vampiric Seduction:</h3>
<p>Vampires, those immortal creatures of the night, have long been emblematic of forbidden desire and unending allure. Emerging from the depths of various cultures' folklore, the vampire has become a cultural icon synonymous with sensuality and death. While their traits vary depending on the mythos, they typically possess supernatural strength, hypnotic abilities, and the need to feed on human blood to survive.</p>
<p>The allure of vampires is rooted in the juxtaposition of their dark, enigmatic nature with the idea of eternal life and youthful beauty. From Bram Stoker's iconic "Dracula" to Anne Rice's "The Vampire Chronicles," literature and cinema have consistently portrayed vampires as charismatic and tormented figures, often blurring the lines between hero and villain. The romanticism associated with the tragic immortality of vampires has ignited a fascination with their existence and the ethical dilemmas surrounding their existence.</p>

<h3>The Witching Hour:</h3>
<p>Witches, on the other hand, are practitioners of magic, often depicted as powerful spellcasters with an affinity for the mystical forces of the universe. Throughout history, witches have been both revered and reviled, celebrated for their supposed ability to commune with the supernatural and condemned as agents of malevolent forces. From Shakespeare's "Macbeth" to modern television shows like "Charmed," witches have taken on various forms, but their connection to magic remains a constant.</p>
<p>Witchcraft is inherently linked to nature, intuition, and the manipulation of energy. Whether concocting potions, casting spells, or reading the stars, witches tap into hidden dimensions to shape the world around them. The archetype of the witch is often associated with the empowerment of women and marginalized groups, offering a subversive alternative to societal norms. This subtext has added depth to the appeal of witches and their enduring popularity.</p>

<h3>A Dance of Shadows and Light:</h3>
<p>The convergence of vampires and witches in various stories has led to intriguing narratives that explore the interplay between darkness and light, power and vulnerability, desire and danger. The dynamics between these two archetypes have birthed stories of forbidden romances, alliances forged in the crucible of adversity, and battles that span the realms of the living and the supernatural.</p>
<p>One can think of the famous example of the "Twilight" series by Stephenie Meyer, where the love between the vampire Edward Cullen and the human Bella Swan is at the heart of the story. This love transcends the challenges posed by Edward's vampiric nature and Bella's human vulnerability, representing the tension between different worlds and desires.</p>
<p>In pop culture, the clash between vampires and witches often underscores deeper themes of identity, choices, and the price of power. These narratives invite us to contemplate the nature of good and evil, the fluidity of morality, and the complexities of our desires.</p>

<h3>Conclusion:</h3>
<p>The duel between vampires and witches encapsulates the dichotomy of human existence – the desire for power, eternal life, and passion, set against the moral quandaries and consequences that come with those desires. These archetypes resonate with us because they embody our own struggles with temptation, identity, and the search for meaning.</p>
<p>While vampires and witches may remain creatures of fiction, their enduring appeal reflects our fascination with the enigmatic and the supernatural. Whether we find ourselves captivated by the allure of the vampire's eternal night or drawn to the mystique of the witch's arcane power, these archetypes continue to cast their spell upon our collective imagination, reminding us that within the shadows and magic, we can explore the depths of our own humanity.</p>
""")

        page8 = Page(title = "Spellbooks", author="yu1234", text=\
"""<h3>The Enigmatic Allure of Spellbooks in the World of Magic</h3>
<p>In the realm of magic, where the mystical and the mundane intertwine, few artifacts hold as much fascination and power as spellbooks. These ancient tomes, bound in leather, adorned with intricate symbols, and whispered to be repositories of arcane knowledge, have captured the imagination of both mages and the curious alike for centuries. As gateways to hidden realms of incantations and enchantments, spellbooks stand as a testament to humanity's ceaseless pursuit of the unknown and the extraordinary.</p>

<h3>The Origins of Spellbooks: Portals to the Arcane</h3>
<p>The origins of spellbooks can be traced back to the earliest civilizations where oral traditions were transcribed into written form, allowing knowledge to be preserved and passed down through generations. As societies evolved, so did the art of magic. Spellbooks emerged as repositories of spells, rituals, and invocations, offering insight into the subtle interplay between the natural and supernatural realms. These books became repositories of not only practical magical knowledge but also reflections of the cultures and beliefs that spawned them.</p>

<h3>The Structure and Content of Spellbooks</h3>
<p>Spellbooks, both in fiction and reality, are typically characterized by their unique design and organization. Many often feature ornate covers adorned with sigils, runes, and mystic symbols, designed to protect the sacred knowledge within. The content of these books spans a vast array of magical practices, from elemental manipulation and divination to healing spells and hexes. The spells themselves can range from simple incantations requiring mere words to complex rituals that demand rare ingredients, precise timing, and unwavering focus.</p>

<h3>Guardians of Secrets: Spellbooks and Their Keepers</h3>
<p>Throughout history, spellbooks have been associated with legendary sorcerers, wise witches, and enigmatic wizards. These figures are often depicted as possessing immense power and responsibility, guarding the knowledge contained within their spellbooks from those who would misuse it. In tales of high fantasy, spellbooks are sometimes even sentient, forging a unique bond with their keepers and bestowing insight and guidance in moments of need.</p>

<h3>The Modern Interpretation: From Fantasy to Reality</h3>
<p>In modern times, while we might not witness spellbooks literally flying off shelves or unleashing bolts of lightning, the concept of spellbooks has transcended fiction. Various contemporary magical practices, such as Wicca and modern witchcraft, involve the use of personal grimoires or spellbooks. These modern interpretations often combine traditional magical knowledge with individual experiences, creating a unique blend of mysticism and personal empowerment.</p>

<h3>Unlocking the Potential: The Role of Intent and Belief</h3>
<p>Regardless of whether one views spellbooks as fictional constructs or genuine tools of magic, their essence lies in the power of intention and belief. A spell is not merely a string of words or a sequence of actions; it's a conduit through which one's intention flows into the fabric of reality. The belief in the effectiveness of a spell, combined with focused intent and emotion, is often considered the cornerstone of successful magical workings.</p>

<h3>A Journey into Mystery and Wonder</h3>
<p>Spellbooks embody the allure of the unknown, beckoning us to explore realms beyond the tangible and comprehend the forces that shape our world. Whether as symbols of ancient wisdom, repositories of forgotten lore, or personal records of individual experiences, spellbooks continue to captivate our imagination and connect us to the ancient, magical narratives that have shaped human history.</p>
<p>As we turn the pages of these enchanted volumes, we are reminded that the mysteries of the universe are vast and ever-unfolding. Whether we find ourselves weaving intricate incantations or simply basking in the enchanting tales spun within these pages, spellbooks remain an enduring testament to humanity's eternal fascination with the mystical and the extraordinary.</p>
""")

        page9 = Page(title="Magic Familiars", author="marc123", text=\
"""<h3>Magic Familiars: A Journey into Enchanted Bonds</h3>
<p>Throughout the annals of history and across diverse cultures, magic has woven its threads into the fabric of human existence. In the realm of sorcery and mysticism, one intriguing element stands out: the concept of magic familiars. These enigmatic companions have fascinated and inspired both practitioners of the arcane arts and curious minds alike. In this exploration, we delve into the mystique surrounding magic familiars, uncovering their origins, roles, and the enduring allure they hold in the world of magic.</p>

<h3>Origins and Evolution: A Historical Perspective</h3>
<p>The origins of magic familiars can be traced back to ancient civilizations, where the bond between humans and animals was deeply intertwined with spiritual beliefs. In many cultures, animals were seen as conduits to the supernatural, possessing a connection to otherworldly realms that humans could tap into. These animals were often revered as messengers or protectors, bridging the gap between the mortal world and the mystical.</p>
<p>As history progressed, the concept of familiars became more closely associated with witchcraft and the practice of magic. During the witch trials of the Middle Ages and the Early Modern Period, familiars were often depicted as demonic entities that aided witches in their dark deeds. This negative portrayal solidified the association between magic practitioners and their animal companions, leading to widespread fear and persecution.</p>
<p>However, not all depictions of familiars were sinister. In some cultures, magic familiars were considered benevolent spirits or guardian spirits that assisted in casting spells, providing guidance, and even offering protection. The concept of a trusted companion that aids the practitioner in their magical endeavors transcended the realm of darkness and persisted as a beacon of positive supernatural connection.</p>

<h3>The Role of Magic Familiars: Beyond the Mundane</h3>
<p>Magic familiars play multifaceted roles in the lives of practitioners, both symbolically and practically. Symbolically, familiars often represent the bridge between the material and spiritual worlds. They embody the intuitive, primal, and instinctual aspects of nature that magic seeks to tap into. In this sense, familiars are not merely pets or assistants; they are conduits of magical energy and sources of guidance in a chaotic world.</p>
<p>Practically, familiars are believed to enhance a magician's abilities by lending their unique qualities to the spellcasting process. Their presence can aid in channeling energy, intensifying focus, and amplifying the intentions behind the magic. Familiars are seen as loyal partners who share an intimate bond with their human counterparts, working together to achieve magical feats that might be difficult to accomplish alone.</p>

<h3>Modern Perspectives and Interpretations</h3>
<p>In contemporary times, the perception of magic familiars has evolved. While the notion of a physical animal companion aiding in spellcasting is still embraced by some practitioners, others view familiars as metaphorical representations of inner strengths and instincts. This shift in perspective reflects the broader evolution of magic from rigid rituals to more intuitive and personalized practices.</p>
<p>Additionally, the symbolism of familiars has expanded to encompass a wider range of beings, including mythical creatures, spirits, and even elemental forces. The modern interpretation of a familiar is not limited to the animal kingdom; it embraces the interconnectedness of all living and spiritual entities.</p>

<h3>The Enduring Allure of Magic Familiars</h3>
<p>The allure of magic familiars endures because they embody the timeless desire for connection, understanding, and guidance. Whether seen as literal companions or symbolic representations, familiars tap into a universal longing for a deeper bond with the natural and supernatural realms. In a world that often feels detached from the mystic, familiars provide a conduit to the unseen, a reminder that magic is not merely a forgotten art but a living, breathing force that continues to shape human perception.</p>
<p>In conclusion, magic familiars remain a captivating aspect of the magical landscape, weaving together history, spirituality, and the ever-evolving nature of human beliefs. Their roles have transformed over time, adapting to cultural shifts and emerging paradigms. Yet, at their core, familiars remain vessels of enchantment, guiding practitioners on a journey of self-discovery and connection with the arcane forces that surround us.</p>
""")

        page10 = Page(title="Famous Witches", author="marc123", text=\
"""
<h3>Chronicles of Famous Witches Throughout History</h3>
<p>Throughout history, witches have fascinated and captivated human imagination. These enigmatic figures have traversed the fine line between reality and myth, bewitching both the minds of their contemporaries and the generations that followed. From ancient legends to modern interpretations, famous witches have left an indelible mark on cultures across the globe. This article embarks on a journey through time to explore some of the most renowned witches in history, shedding light on their stories, beliefs, and lasting legacies.</p>

<h3>1. Circe - The Mythical Sorceress</h3>
<p>In ancient Greek mythology, Circe stands as one of the most iconic witches. A daughter of the sun god Helios, she was known for her mastery of magic and her residence on the isolated island of Aeaea. Circe is famously associated with transforming Odysseus' men into swine in Homer's "Odyssey." Her story has transcended time, inspiring countless artistic interpretations that delve into the complexities of power, temptation, and enchantment.</p>

<h3>2. Morgan le Fay - Arthurian Legend</h3>
<p>The Arthurian legend introduces us to Morgan le Fay, a character who embodies the dual nature of magic. Often depicted as both a healer and a sorceress, Morgan is King Arthur's half-sister. Her character evolved over time, from being a benevolent healer to a cunning enchantress. Her tale exemplifies the ambivalence of magic, showcasing its potential for both good and ill.</p>

<h3>3. Tituba - Salem Witch Trials</h3>
<p>The infamous Salem Witch Trials of 1692 cast a long shadow on the history of witchcraft. Among those accused was Tituba, a Caribbean slave and a central figure in the witch hysteria that gripped colonial Massachusetts. Tituba's "confessions" of practicing witchcraft fueled the mass hysteria and accusations that followed. Her story serves as a haunting reminder of the dangers of unfounded accusations and societal hysteria.</p>

<h3>4. Marie Laveau - The Voodoo Queen</h3>
<p>Moving into the realm of folk magic and spirituality, Marie Laveau emerges as a prominent figure in the history of witchcraft. Hailing from New Orleans, she was known as the "Voodoo Queen" and became a central figure in the city's Voodoo traditions. Laveau's practices blended African spiritual traditions with Catholicism, creating a unique and influential form of magic that continues to captivate curious minds to this day.</p>

<h3>Conclusion</h3>
<p>Famous witches throughout history have woven a rich tapestry of narratives, beliefs, and cultural significance. From the mythical enchantresses of ancient Greece to the real-life practitioners of magic, these figures continue to captivate our imagination and challenge our perceptions of the mystical. Their stories remind us of the complex interplay between power, knowledge, and the human longing for connection with the unknown. As we delve into the chronicles of famous witches, we uncover not only their tales but also the eternal fascination that magic and witchcraft evoke.</p>
""")

        page_list = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10]
        db.session.add_all(page_list)
        db.session.commit()



        print("Adding edits")       
        for i in range(16):
            page = rc(page_list)
            text = page.text
            split_list = text.split('\n')
            index = ri(1,len(split_list))
            split_list.insert(index, "<p>GONNA SPRINKLE SOME OF MY MAGIC HEHEHEHE</p>")
            edit_text3 = '\n'.join(split_list)

            if i < 7:
                edit_text1 = text.replace("magic", "MAAAGICCCC", 3)
                if text != edit_text1:
                    edit_text = edit_text1
                else:
                    edit_text = edit_text3               
            else : 
                edit_text2 = text.replace("witch", "WIIITCHAAE", 3)
                if text != edit_text2:
                    edit_text = edit_text2
                else:
                    edit_text = edit_text3
            new_edit = page.create_edit(new_text = edit_text, user_id = ri(1,3))
                          
            page.text = edit_text
            # print(f"----------{i}-------------")
            # print(page.text)
            db.session.add(new_edit)
            db.session.commit()



        print("Finished Seeding")
