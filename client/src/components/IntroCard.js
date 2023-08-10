import React from "react";

const text = ` is a modern pagan religious movement that emerged in the mid-20th century  It draws inspiration from pre-Christian and folkloric traditions, emphasizing a connection with nature, rituals, and reverence for the divine. Wiccans often follow a duotheistic belief system centered around a god and goddess, representing masculine and feminine energies.  Central to Wicca is the practice of magic, which is seen as a way to influence the natural world and personal circumstances. Rituals and ceremonies are performed according to a seasonal cycle, including Sabbats (major holidays) and Esbats (lunar-based rituals). These rituals involve the use of tools, such as athames (ritual knives), wands, and chalices, as well as the casting of circles to create sacred space.  Wiccans commonly adhere to the Wiccan Rede, a moral guideline that states, "An it harm none, do what ye will," advocating for actions that do not cause harm to oneself or others. Additionally, the Law of Threefold Return suggests that energy put into the world, whether positive or negative, returns to the sender threefold.  Wicca is diverse, with various traditions and interpretations, such as Gardnerian, Alexandrian, and eclectic Wicca. It places a strong emphasis on personal experience, individual spirituality, and a deep connection with the natural world.`
function IntroCard(){

    return(
        <div className="container mb-5">
            <img src="https://www.wikihow.com/images/thumb/6/6a/Become-a-Wiccan-Step-3-Version-2.jpg/v4-460px-Become-a-Wiccan-Step-3-Version-2.jpg.webp" alt="template" className='float-start img-shadow' style={{width : '300px', marginRight : '10px'}}/>
            <span className="fst-italic fs-4">Wicca</span><span className="">{text}</span>
        </div>
    )
}

export default IntroCard