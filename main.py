from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
canvas = Canvas(tk, width = 1250, height = 600)
canvas.pack()
timeline = PhotoImage(file="timeline.png")
cambbg = PhotoImage(file="cambrian.png").zoom(2, 2).subsample(5, 5)
ordobg = PhotoImage(file="ordovician.png").zoom(2, 2).subsample(3, 3)
silubg = PhotoImage(file="silurian.png").subsample(7, 7)
carbbg = PhotoImage(file="carboniferous.png").subsample(2, 2)
devobg = PhotoImage(file="devonian.png").zoom(3, 3).subsample(4, 4)
permbg = PhotoImage(file="permian.png").zoom(5, 5).subsample(4, 4)
triabg = PhotoImage(file="triassic.png").zoom(2, 2).subsample(3, 3)
jurabg = PhotoImage(file="jurassic.png").subsample(4, 4)
cretbg = PhotoImage(file="cretaceous.png")
palebg = PhotoImage(file="paleogene.png")
neogbg = PhotoImage(file="neogene.png").zoom(5, 5).subsample(4, 4)

screen = "timeline"
era = 12

x = 0
y = 0

geninfo = ["The Cambrian Period is most notable for the Cambrian Explosion—a rapid diversification of multicellular life, especially in marine environments. Most major animal phyla first appeared during this time. Trilobites dominated ecosystems, while early chordates and reef-building organisms also emerged. Earth's land surface remained largely barren, with continents arranged near the equator.", "Marine biodiversity continued to expand, with the proliferation of giant mollusks, bryozoans, crinoids, and the first true coral reefs. Jawless fish diversified, and early land plants and fungi began colonizing moist terrestrial environments. Atmospheric CO2 levels were high, but a glaciation event at the end of the period triggered a major ice age and sea level drop, resulting in the second-largest mass extinction in Earth's history.", "Following the Ordovician extinction, marine ecosystems rebounded, with the rise of jawed fish and continued reef expansion. The first vascular land plants (e.g., Cooksonia) appeared, allowing more widespread terrestrial colonization. Arthropods such as millipedes and arachnids likely became the first animals to inhabit land. Earth’s climate stabilized, with warm shallow seas covering much of the planet.", "Known as the “Age of Fishes,” the Devonian saw remarkable diversity in both jawed and jawless fish, including placoderms and lobe-finned species. Extensive forests of early vascular plants like lycophytes and ferns developed, significantly altering the carbon cycle and atmospheric composition. Tetrapods evolved from lobe-finned fish, initiating the vertebrate transition to land. The period ended with a series of extinction events, possibly linked to widespread deoxygenation in the oceans.", "Characterized by vast swampy forests and high atmospheric oxygen levels, the Carboniferous produced immense coal-forming deposits. Giant arthropods like massive millipedes, dragonflies, centipedes and early amphibians flourished in humid, tropical environments. The first egg-laying vertebrates appeared, allowing vertebrates to reproduce fully on land. The supercontinent Pangaea began to form, affecting global climate patterns.", "The Permian Period witnessed the diversification into early reptiles, synapsids (like Dimetrodon), and therapsids (mammal-like reptiles). Interior regions of Pangaea became arid due to its massive size and distance from oceanic moisture. Gymnosperms and seed ferns dominated the flora. The period ended with the largest mass extinction in Earth's history, wiping out over 90% of marine species and 70% of terrestrial vertebrates, likely due to massive volcanism, climate change, and ocean acidification.", "Life rebounded in the Triassic with the emergence of archosaurs, including the first dinosaurs, pterosaurs, and crocodilians. Mammal ancestors also evolved during this time. Pangaea’s unified landmass contributed to harsh, seasonal climates, while conifers became dominant in terrestrial ecosystems. The period ended with another extinction event, likely caused by volcanic activity, setting the stage for dinosaur dominance.", "The breakup of Pangaea into Laurasia and Gondwana led to rising sea levels and a warm, humid climate. Dinosaurs diversified into iconic forms such as sauropods, theropods, and stegosaurs. The first true birds evolved from small feathered theropods. Marine ecosystems were populated by ichthyosaurs, plesiosaurs, and ammonites, while forests of cycads, ginkgos, and conifers thrived on land.", "The Cretaceous saw the continued dominance of dinosaurs and the rise of flowering plants, which transformed terrestrial ecosystems. Avian dinosaurs (true birds) became more diverse, and pollinator insects such as bees appeared. Continental drift continued to reshape Earth’s surface, and global sea levels were high. The period ended abruptly with the Chicxulub asteroid impact, leading to the K-T extinction event that wiped out non-avian dinosaurs and many marine species.", "Mammals rapidly diversified and filled ecological niches left vacant by dinosaurs, giving rise to early primates, cetaceans, ungulates, and carnivores. Birds also radiated into many modern forms. The climate started warm but gradually cooled, with the formation of polar ice caps by the end of the period. Grasslands began to expand, influencing herbivore evolution.", "The Neogene witnessed the further evolution of modern mammals and birds, as well as the expansion of open habitats like savannas and steppes. The ancestors of humans (hominins) appeared in Africa, eventually developing bipedalism and larger brains. Tectonic shifts shaped modern continents and mountain ranges (e.g., the Himalayas). Global cooling intensified, setting the stage for the Quaternary Ice Ages."]
maps = [PhotoImage(file="cambmap.png"), PhotoImage(file="ordomap.png"), PhotoImage(file="silumap.png"), PhotoImage(file="devomap.png"), PhotoImage(file="carbmap.png"), PhotoImage(file="permmap.png"), PhotoImage(file="triamap.png"), PhotoImage(file="juramap.png"), PhotoImage(file="cretmap.png"), PhotoImage(file="palemap.png")]
animalspic = [
    [ImageTk.PhotoImage(Image.open("trilobite.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("anomalocaris.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("brachiopod.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("conodont.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("eurypterid.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("endoceras.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("favosite.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("cooksonia.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("pterapsis.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("dunkleosteus.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("coelacanth.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("tiktaalik.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("temnospondyls.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("meganeura.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("crinoids.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("dimetrodon.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("therapsid.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("helicoprion.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("ichthyosaur.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("herrerasaurus.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("prestosuchus.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("plessie.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("SCAPPERS!!!.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("allosaurus.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("yutyrannus.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("nasutoceratops.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("amargasaurus.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("mastodon.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("smilodon.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("megatherium.png").resize((200, 200)))],
    [ImageTk.PhotoImage(Image.open("bigbird.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("rhino.png").resize((200, 200))), ImageTk.PhotoImage(Image.open("DIEMF.png").resize((200, 200)))]
]

animalsinfo = [["Extinct arthropods with segmented bodies and exoskeletons; highly diverse bottom-dwellers that filled roles from scavengers to predators.", "Anomalocaris was a meter-long, apex predator of the Cambrian seas, known for its spiny grasping limbs, circular toothy mouth, and excellent vision—making it one of Earth’s first complex hunters.", "Brachipods are marine animals with two hard shells and a lophophore (a feeding organ), which thrived on the seafloor and resemble clams, though they are unrelated and filter-feed differently."], ["Conodonts were extinct, eel-like jawless vertebrates that were dangerous hunter, known mostly from their tooth-like microfossils, which are used as key index fossils in dating ancient marine rocks and possesed the sharpest teeth of any animal ever.", "Eurypterids, or 'sea scorpions,' were large, fearsome, aquatic arthropods that lived from the Ordovician to the Permian period; some grew over 2 meters long and were top predators in ancient seas, rivers, and lakes.", "Endoceras was a massive, straight-shelled cephalopod and one of the largest predators of the Ordovician seas. It used jet propulsion and tentacles to hunt trilobites and other marine animals, dominating ocean ecosystems before vertebrate predators emerged."], ["Favosites, a genus of tabulate coral, was significant during the Silurian period for its role in reef-building. Its honeycomb-like skeletons formed large colonies that helped create complex reef ecosystems, providing habitat for many marine species and contributing to biodiversity and carbonate sediment formation.", "Cooksonia was the first known vascular land plant, appearing in the Silurian period. Its importance lies in marking a major evolutionary step—plants moving from water to land. With simple stems and vascular tissue, Cooksonia helped pave the way for complex terrestrial ecosystems by stabilizing soils and beginning the transformation of Earth’s atmosphere.", "As one of the earliest vertebrates with a developed protective skeleton, Pteraspis played a key part in the transition toward more advanced fish and later jawed vertebrates, helping shape early Silurian marine ecosystems."], ["Placoderms were heavily armored, jawed fish that dominated Devonian seas and freshwater environments; they were among the first vertebrates with true jaws, and some like Dunkleosteus grew over 6 meters long, making them top predators of their time.", "Lobe-finned fishes (Sarcopterygians) were a key group in the Devonian, characterized by fleshy, limb-like fins supported by bone.", "Tiktaalik was a transitional species from the Devonian (~375 million years ago) that had both fish and tetrapod features, including fins with wrist-like bones, a flat head, and lungs, making it a key step in the evolution of vertebrates from water to land."], ["Temnospondyls were diverse, early amphibians that first appeared in the Carboniferous period, thriving in aquatic and semi-aquatic environments.", "Meganeura was a giant dragonfly-like insect from the Carboniferous period, with a wingspan of up to 70 cm, one of the first flying animals on Earth, and preying on smaller insects and possibly small vertebrates.", "Crinoids in the Carboniferous were abundant marine animals with stalks and feathery arms that filtered food. They thrived in warm seas and were key reef builders."], ["Synapsids in the Permian were dominant terrestrial vertebrates, including early mammal ancestors like pelycosaurs and therapsids. They showed increasing diversity and adaptations, leading toward more advanced mammal-like features.", "Therapsids in the Permian were advanced synapsids that became dominant land animals. They had more mammal-like traits, such as differentiated teeth and improved jaw structure, and paved the way for mammals.", "During the Permian, sharks spread widely across marine environments, diversifying into many species. They adapted to different habitats, becoming key predators in the oceans worldwide."], ["Ichthyosaurs in the Triassic were among the first large marine reptiles. They evolved quickly after the Permian extinction, adapted for fast swimming, and became dominant ocean predators.", "Early dinosaurs in the Triassic were small to medium-sized, mostly bipedal reptiles. They first appeared late in the period and gradually diversified, laying the foundation for later dinosaur dominance.", "Not true crocodilians, but a group of large, extinct archosaur relatives of crocodilians, that lived during the Triassic and were top predators before dinosaurs became dominant."], ["During the Jurassic, plesiosaurs became dominant marine reptiles, thriving in oceans worldwide. Their adaptations—like powerful flippers and long necks—made them effective swimmers and predators, allowing them to outcompete many other marine reptiles.", "Pterosaurs became the dominant flying vertebrates. Their diverse sizes and shapes allowed them to exploit various aerial niches, mainly hunting fish and small prey, ruling the skies before birds evolved.", "During the Jurassic, theropods became the dominant land predators. They grew larger and more diverse, including famous species like Allosaurus, and played a key role as top carnivores in terrestrial ecosystems."], ["Tyrannosaurs became apex predators in the Late Cretaceous. They dominated terrestrial ecosystems in North America, evolving powerful jaws, strong legs, and keen senses. Their role as top predators marked the peak of theropod evolution before the mass extinction at the end of the Cretaceous.", "Ceratopsians were heavily armored, horned herbivores that thrived in the Late Cretaceous. They formed large herds and were among the most successful plant-eaters of the time, using their frills and horns for defense, display, and possibly combat.", "Although less dominant than in the Jurassic, sauropods remained significant in southern continents like South America. Titanosaurs, a group of sauropods, included some of the largest land animals ever. Their continued success in the Cretaceous shows their adaptability to changing environments."], ["Mastodons were large, tusked relatives of elephants that emerged in the Paleogene and spread across North America and Eurasia. They thrived in forested regions, browsing on shrubs and trees, and became a key part of herbivore communities.", "Saber-toothed cats like Smilodon evolved powerful forelimbs and long, curved canine teeth adapted for slicing flesh. These predators dominated grassland and woodland ecosystems, using stealth and strength to hunt large prey, especially during the later Paleogene and into the Pleistocene.", "Giant ground sloths, such as Megatherium, were slow-moving but massive herbivores that thrived in South America. They played a major role in shaping vegetation and were well adapted to a variety of habitats, from forests to open plains."], ["Terror birds were large, flightless predators that ruled South American ecosystems. With powerful legs and beaks, they could run down and kill smaller animals, filling the role of top terrestrial predator in a continent without large mammalian carnivores for much of the Neogene.", "Rhinos evolved into a wide range of species, including Paraceratherium, the largest land mammal ever. They were dominant herbivores in grasslands and open woodlands, using their size and horns for defense and display.", "Megalodon was a massive predatory shark that dominated Neogene oceans. Likely preying on whales and large fish, it was an apex marine predator with an enormous bite force. Its reign lasted until its extinction in the Pliocene."]]
climateinfo = ["The Cambrian Period featured a warm global climate with high sea levels and an oxygenated atmosphere that supported the rapid diversification of life in the oceans, though the land remained largely barren and dry.", "Initially warm and humid with high atmospheric CO2 levels, the Ordovician saw extensive shallow seas and reef-building, but ended with a massive ice age and global cooling that triggered one of the first major mass extinctions.", "The Silurian climate was relatively stable and warm following the Ordovician glaciation, with rising sea levels and increased oxygen levels in the atmosphere, which helped facilitate the colonization of land by early plants and arthropods.", "Marked by a warm and increasingly oxygenated atmosphere, the Devonian experienced widespread tropical conditions, lush terrestrial vegetation, and periodic anoxic events in oceans that coincided with several extinction pulses.", "The Carboniferous was characterized by a warm, humid climate with high oxygen concentrations that enabled giant insects and dense coal-forming forests, though later glaciations in the southern hemisphere signaled the onset of climate cooling.", "Early Permian conditions were glacial and dry, transitioning into a hotter and more arid supercontinent climate with lower oxygen and rising carbon dioxide levels, culminating in the largest mass extinction in Earth’s history.", "Following the Permian extinction, the Triassic was hot and dry with a stable supercontinental climate, high CO2, and little polar ice, promoting reptile dominance and ending with another mass extinction tied to volcanic activity and climate disruption.", "The Jurassic had a generally warm, humid, and greenhouse-like climate with high sea levels and widespread tropical conditions, encouraging lush vegetation and the rise of dinosaurs and early birds.", "During the Cretaceous, Earth experienced high temperatures, elevated CO2, and little polar ice, creating vast inland seas and flourishing plant and animal life until the dramatic asteroid impact that ended the era.", "The Paleogene began with a warm post-extinction greenhouse climate, peaked with the Paleocene-Eocene Thermal Maximum, and gradually cooled as polar ice sheets began to form and CO2 levels declined.", "Characterized by a long-term cooling trend, the Neogene saw the expansion of grasslands, more seasonal climates, falling CO2 levels, and the development of modern ecosystems as Earth approached the Ice Ages."]

def home():
    canvas.delete("all")
    background = canvas.create_image(0, 200, anchor=NW, image=timeline)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "Are you ready to explore the prehistoric world?")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about each time period!")
    tk.update()
def cambrian():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=cambbg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Cambrian Period, the first geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Cambrian!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(494 - 10, 275 - 10, 494 + 10, 275 + 10, fill = "SlateGray3")
    map = canvas.create_oval(611 - 10, 474 - 10, 611 + 10, 474 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(742 - 10, 186 - 10, 742 + 10, 186 + 10, fill = "SlateGray3")
    tk.update()
def ordovician():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=ordobg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Ordovician Period, the second geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Ordovician!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(521 - 10, 408 - 10, 521 + 10, 408 + 10, fill = "SlateGray3")
    map = canvas.create_oval(435 - 10, 554 - 10, 435 + 10, 554 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(639 - 10, 178 - 10, 639 + 10, 178 + 10, fill = "SlateGray3")
    tk.update()
def silurian():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=silubg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Silurian Period, the third geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Silurian!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(629 - 10, 438 - 10, 629 + 10, 438 + 10, fill = "SlateGray3")
    map = canvas.create_oval(464 - 10, 500 - 10, 464 + 10, 500 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(617 - 10, 160 - 10, 617 + 10, 160 + 10, fill = "SlateGray3")
    tk.update()
def devonian():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=devobg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Devonian Period, the fourth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Devonian!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(597 - 10, 458 - 10, 597 + 10, 458 + 10, fill = "SlateGray3")
    map = canvas.create_oval(353 - 10, 537 - 10, 353 + 10, 537 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(724 - 10, 175 - 10, 724 + 10, 175 + 10, fill = "SlateGray3")
    tk.update()
def carboniferous():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=carbbg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Carboniferous Period, the fifth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Carboniferous!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(716 - 10, 307 - 10, 716 + 10, 307 + 10, fill = "SlateGray3")
    map = canvas.create_oval(541 - 10, 526 - 10, 541 + 10, 526 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(573 - 10, 189 - 10, 573 + 10, 189 + 10, fill = "SlateGray3")
    tk.update()
def permian():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=permbg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Permian Period, the sixth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Permian!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(584 - 10, 354 - 10, 584 + 10, 354 + 10, fill = "SlateGray3")
    map = canvas.create_oval(782 - 10, 497 - 10, 782 + 10, 497 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(691 - 10, 178 - 10, 691 + 10, 178 + 10, fill = "SlateGray3")
    tk.update()
def triassic():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=triabg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Triassic Period, the seventh geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Triassic!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(422 - 10, 356 - 10, 422 + 10, 356 + 10, fill = "SlateGray3")
    map = canvas.create_oval(497 - 10, 191 - 10, 497 + 10, 191 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(772 - 10, 381 - 10, 772 + 10, 381 + 10, fill = "SlateGray3")
    tk.update()
def jurassic():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=jurabg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Jurassic Period, the eighth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Jurassic!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(641 - 10, 464 - 10, 641 + 10, 464 + 10, fill = "SlateGray3")
    map = canvas.create_oval(393 - 10, 556 - 10, 393 + 10, 556 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(761 - 10, 242 - 10, 761 + 10, 242 + 10, fill = "SlateGray3")
    tk.update()
def cretaceous():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=cretbg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Cretaceous Period, the ninth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Cretaceous!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(694 - 10, 412 - 10, 694 + 10, 412 + 10, fill = "SlateGray3")
    map = canvas.create_oval(473 - 10, 515 - 10, 473 + 10, 515 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(806 - 10, 184 - 10, 806 + 10, 184 + 10, fill = "SlateGray3")
    tk.update()
def paleogene():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=palebg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Palegene Period, the tenth geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font=("Purisa", 16), text="Click to learn more about the Paleogene!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(789 - 10, 396 - 10, 789 + 10, 396 + 10, fill = "SlateGray3")
    map = canvas.create_oval(571 - 10, 538 - 10, 571 + 10, 538 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(675 - 10, 176 - 10, 675 + 10, 176 + 10, fill = "SlateGray3")
    tk.update()
def neogene():
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=neogbg)
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is the Neogene Period, the eleventh geologic time period.")
    title2 = canvas.create_text((1125//2), 125, font = ("Purisa", 16), text="Click to learn more about the Neogene!")
    gen = canvas.create_oval(300 - 10, 175 - 10, 300 + 10, 175 + 10, fill = "SlateGray3")
    ani = canvas.create_oval(756 - 10, 457 - 10, 756 + 10, 457 + 10, fill = "SlateGray3")
    map = canvas.create_oval(571 - 10, 572 - 10, 571 + 10, 572 + 10, fill = "SlateGray3")
    atmo = canvas.create_oval(794 - 10, 220 - 10, 794 + 10, 220 + 10, fill = "SlateGray3")
    tk.update()

buttons = [[[300, 175],[494, 275],[611, 474],[742, 186]], [[300, 175],[521, 408],[435, 554],[639, 178]],[[300, 175],[629, 438],[464, 500],[617, 160]],[[300, 175],[597, 458],[353, 537],[724, 175]],[[300, 175],[716, 307],[541, 526],[573, 189]],[[300, 175],[584, 354],[782, 497],[691, 178]],[[300, 175],[422, 356],[497, 191],[772, 381]],[[300, 175],[641, 464],[393, 556],[761, 242]],[[300, 175],[694, 412],[473, 515],[806, 184]],[[300, 175],[789, 396],[571, 538],[675, 176]],[[300, 175],[756, 457],[571, 572],[794, 220]]]

periods = [cambrian, ordovician, silurian, devonian, carboniferous, permian, triassic, jurassic, cretaceous, paleogene, neogene]

def generalinfo(era):
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    title1 = canvas.create_text((1125//2), 300, font = ("Purisa", 16), text = geninfo[era], width = 600)
    tk.update()
def animals(era):
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    img1 = canvas.create_image((1125//4), 150, anchor=N, image=animalspic[era][0])
    img2 = canvas.create_image((1125//2), 150, anchor=N, image=animalspic[era][1])
    img3 = canvas.create_image((1125*3//4), 150, anchor=N, image=animalspic[era][2])
    canvas.create_text((1125//4), 400, anchor = N, font = ("Purisa", 14), text = animalsinfo[era][0], width = 200)
    canvas.create_text((1125//2), 400, anchor = N, font = ("Purisa", 14), text = animalsinfo[era][1], width = 200)
    canvas.create_text((1125*3//4), 400, anchor = N, font = ("Purisa", 14), text = animalsinfo[era][2], width = 200)
    tk.update()
def map(era):
    canvas.delete("all")
    title1 = canvas.create_text((1125//2), 100, font = ("Purisa", 16), text = "This is what the Earth looked like during the "+ periods[era].__name__[0].upper() + periods[era].__name__[1:] + " period.")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    background = canvas.create_image((1125//2), 150, anchor=N, image=maps[era])
    tk.update()
def climate(era):
    canvas.delete("all")
    backtext = canvas.create_text(30, 20, anchor = NW, font = ("Purisa", 24), text = " Return ")
    backbox = canvas.create_rectangle(canvas.bbox(backtext),fill="white")
    canvas.tag_lower(backbox,backtext)
    canvas.create_text((1125//2), 200, font = ("Purisa", 16), text = climateinfo[era], width = 400)

def click(c):
    global screen
    global era
    x = c.x
    y = c.y
    if screen == "timeline":
        if y >= 200 and y <= 250:
            if x >= 0 and x <= 110:
                screen = "cambrian"
                cambrian()
            elif x >= 111 and x <= 225:
                screen = "ordovician"
                ordovician()
            elif x >= 226 and x <= 335:
                screen = "silurian"
                silurian()
            elif x >= 336 and x <= 447:
                screen = "devonian"
                devonian()
            elif x >= 448 and x <= 582:
                screen = "carboniferous"
                carboniferous()
            elif x >= 448 + 134 and x <= 559 + 134:
                screen = "permian"
                permian()
            elif x >= 560 + 134 and x <= 672 + 134:
                screen = "triassic"
                triassic()
            elif x >= 673 + 134 and x <= 783 + 134:
                screen = "jurassic"
                jurassic()
            elif x >= 784 + 134 and x <= 902 + 134:
                screen = "cretaceous"
                cretaceous()
            elif x >= 903 + 134 and x <= 1014 + 134:
                screen = "paleogene"
                paleogene()
            else:
                screen = "neogene"
                neogene()
    elif screen == "info":
        if y >= 20 and y <= 60 and x >= 30 and x <= 160:
            screen = periods[era].__name__
            periods[era]()
    else:
        if y >= 20 and y <= 60 and x >= 30 and x <= 160:
            screen = "timeline"
            home()
        else:            
            if  ((x - buttons[era][0][0])**2 + (y - buttons[era][0][1])**2)**0.5 <= 10:
                screen = "info"
                generalinfo(era)
            elif ((x - buttons[era][1][0])**2 + (y - buttons[era][1][1])**2)**0.5 <= 10:
                screen = "info"
                animals(era)
            elif ((x - buttons[era][2][0])**2 + (y - buttons[era][2][1])**2)**0.5 <= 10:
                screen = "info"
                map(era)
            elif ((x - buttons[era][3][0])**2 + (y - buttons[era][3][1])**2)**0.5 <= 10:
                screen = "info"
                climate(era)
    for i in range(0, 11):
        if screen == periods[i].__name__:
            era = i
            break
tk.bind("<Button-1>", click)

home()
while True:
    tk.update()
