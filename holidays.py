
HOLIDAYS = {}

for month in range(1, 12+1):
	
	month_dict = {}
	
	for day in range(1, 31+1):
		month_dict[day] = []
	
	HOLIDAYS[month] = month_dict

def add_holiday(month, day, name, desc, img=None):
	HOLIDAYS[month][day].append({
		"name": name,
		"desc": desc,
		"img": img
	})

# -------- #
# HOLIDAYS #
# -------- #

''' =TEMPLATE=
add_holiday(1, 1,
	"",
	""
)
'''

add_holiday(1, 1,
	"New Year's Day",
	"We've made it another spin around the sun (according to the Gregorian calendar)! Make some resolutions, watch a parade or football game, or just take it easy today!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/New-Years-Day-iStock-472023065-750x375.jpg"
)

add_holiday(1, 5,
	"Epiphany Eve",
	"Also known as the Twelfth Day of Christmas. For many hardcore Christmas fans, today marks the final day of the Christmas season, and a traditional last day to keep up Christmas decorations. It's also the day before the Christian feast of Epiphany."
)



add_holiday(2, 14,
	"Valentine's Day",
	"A day for celebrating all the different kinds of love in your life. Spend today with those you love!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/Valentines-Day-iStock-641045592-750x375.jpg"
)



add_holiday(3, 17,
	"Saint Patrick's Day",
	"A day for celebrating Irish culture and heritage. Wear something green today!",
	img="https://nationaltoday.com/wp-content/uploads/2019/03/st-patricks-day-1200x834.jpg.webp"
)



add_holiday(5, 5,
	"Cinco de Mayo",
	"A day for celebrating Mexican culture and heritage, commemorating the Mexican army's victory in the 1862 Battle of Puebla. Celebrate by eating some Mexican cuisine or listening to some Mexican music today!",
	img="https://nationaltoday.com/wp-content/uploads/2021/05/cinco-1-1200x834.jpg"
)

add_holiday(5, 19,
	"Malcolm X Day",
	"A day to honor the life and work of revolutionary civil rights leader Malcolm X (usually observed on his birthday, May 19th, but in some places celebrated on the third Friday in May). Take the opportunity to learn something new about Malcolm X today.",
	img="https://nationaltoday.com/wp-content/uploads/2022/07/30-Malcolm-X-Day-1200x834.jpg.webp"
)



add_holiday(6, 8,
	"World Oceans Day",
	"Coordinated by The Ocean Project to raise awareness of the importance of our oceans.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/World-Oceans-Day-750x375.jpg"
)
add_holiday(6, 8,
	"National Best Friends Day",
	"A day for appreciating your best friends!"
)
add_holiday(6, 8,
	"Name Your Poison Day",
	"Celebrate by having your favorite unhealthy drink, whether it be alcoholic, caffienated, sugary, or otherwise."
)

add_holiday(6, 9,
	"National Donald Duck Day",
	"Donald Duck made his first screen appearance on June 9th, 1934, in the Silly Symphonies short film *The Wise Little Hen*.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/03/National-Donald-Duck-Day-iStock-1189631831-750x375.jpg"
)
add_holiday(6, 9,
	"National Strawberry Rhubarb Pie Day",
	"Eat a slice of strawberry rhubarb pie today!"
)
add_holiday(6, 9,
	"Eat Flexitarian Day",
	"The flexitarian (or semi-vegetarian) diet focuses on plant-based foods with occasional inclusion of meat. Take the opportunity to try out a plant-based meal that you don't normally eat today."
)

add_holiday(6, 10,
	"National Iced Tea Day",
	"Have a glass of iced tea today!",
	img="https://nationaltoday.com/wp-content/uploads/2021/06/Iced_Tea_2-1200x834.jpg"
)
add_holiday(6, 10,
	"National Herbs and Spices Day",
	"A day for appreciating the herbs and spices that give our food so much flavor."
)
add_holiday(6, 10,
	"National Black Cow Day",
	"More commonly known as a root beer float, a black cow is a dessert beverage created by adding scoops of vanilla ice cream to root beer. Celebrate by having one today!"
)
add_holiday(6, 10,
	"National Ballpoint Pen Day",
	"A day for appreciating the humble yet ubiquitous writing utensil."
)

add_holiday(6, 11,
	"Kamehameha Day",
	"A major holiday in Hawai'i, today celebrates King Kamehameha the Great, who unified the Kingdom of Hawai'i in 1795. Traditions include parades, hula dancing, feasts, and lots of leis.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/09/Kamehameha-Day-750x375.jpg"
)
add_holiday(6, 11,
	"National Corn on the Cob Day",
	"A day honoring the most traditional method of consuming the United States' biggest crop, just in time for the summer harvest. Eat some corn on the cob today!"
)
add_holiday(6, 11,
	"National German Chocolate Cake Day",
	"A day honoring the famous cake invented by (and named after) Samuel German in 1852. Celebrate by having a slice today!"
)
add_holiday(6, 11,
	"International Yarn Bombing Day",
	"Yarn bombing is a style of street art performed by knitting/crocheting onto public structures like benches, statues, and trees, meant to be a less destructive method of graffiti than spray paint. Look for some yarn bombing around your area today!"
)

add_holiday(6, 12,
	"Superman Day",
	"A day honoring D.C.'s most iconic character. Some comic stores celebrate the day by giving out free Superman comics or otherwise running Superman-related promotions - check your local comic store!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/Superman-Day-PB-7269293_1920-750x375.jpg"
)
add_holiday(6, 12,
	"International Falafel Day",
	"A day celebrating the popular Middle Eastern vegan street food. Eat some falafel today!"
)
add_holiday(6, 12,
	"World Day Against Child Labor",
	"Established by the International Labor Organization to raise awareness of child labor in the modern day and call for an end to child labor in all its forms."
)

add_holiday(6, 13,
	"World Softball Day",
	"A day to celebrate and promote the sport of softball. Watch a softball game today!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/08/World-Softball-Day-PB-1827986_1920-750x375.jpg"
)
add_holiday(6, 13,
	"International Albinism Awareness Day",
	"Organized by the United Nations to call for awareness and acceptance of those living with albinism."
)
add_holiday(6, 13,
	"National Weed Your Garden Day",
	"If you have a garden, make sure you weed it today!"
)
add_holiday(6, 13,
	"International Axe Throwing Day",
	"A day to celebrate and promote the sport/hobby of axe throwing. Many axe throwing clubs run promotions or even free admission days today!"
)

add_holiday(6, 14,
	"Flag Day",
	"A day commemorating the adoption of the flag of the United States on June 14th, 1777. Today also marks the birthday of the United States Army, founded on June 14th, 1775.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2017/03/Flag-Day-United-States-iStock-509426588-750x375.jpg"
)
add_holiday(6, 14,
	"World Blood Donor Day",
	"Created by W.H.O. to raise awareness of the importance of donating blood, held on June 14th to commemorate the birthday of Karl Landsteiner, the doctor who discovered blood transfusion. Many blood drives are held today, so consider donating!"
)
add_holiday(6, 14,
	"International Bath Day",
	"A day celebrating the practice of taking a long, relaxing bath. It commemorates the legend of Archimedes discovering that an object's mass can be measured via water displacement while taking a bath on June 14th. Try bathing instead of showering today!"
)
add_holiday(6, 14,
	"National Strawberry Shortcake Day",
	"Held at peak strawberry season to celebrate the iconic summer dessert. Have a strawberry shortcake today!"
)

add_holiday(6, 15,
	"Nature Photography Day",
	"Founded by the North American Nature Photography Association, everybody is encouraged to get a little closer to nature today by participating in nature photography. Grab your phone or camera and see what shots you can take!",
	img="https://nationaltoday.com/wp-content/uploads/2021/06/Nature-Photography1-1200x834.jpg"
)
add_holiday(6, 15,
	"Global Wind Day",
	"A day for appreciating the importance and benefits of clean wind power."
)
add_holiday(6, 15,
	"World Elder Abuse Awareness Day",
	"A day to raise awareness of the prevalent issue of elder abuse."
)

add_holiday(6, 16,
	"Bloomsday",
	"James Joyce's classic 1922 novel *Ulysses* follows protagonist Leopold Bloom over the course of a single day: June 16th, 1904. Fans of Joyce have commemorated the day as Bloomsday, and celebrate it by honoring the author's life and works. The event is most popular in Dublin, Ireland (Joyce's birthplace), where it is celebrated with a week-long festival.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2017/04/Bloomsday_g-750x375.jpg"
)
add_holiday(6, 16,
	"National Fudge Day",
	"A day to honor the simple confection, which has many varieties but can be made in its most basic form with just three ingredients: sugar, butter, and milk. Celebrate the day by eating some fudge today, or even make some of your own!"
)

add_holiday(6, 17,
	"National Eat Your Vegetables Day",
	"A day for appreciating the nutritious and ever-important food group. Eat your veggies today!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/03/National-Eat-Your-Vegetables-Day-750x375.jpg"
)
add_holiday(6, 17,
	"Global Garbage Man Day",
	"A day to appreciate and celebrate the sanitation workers around the globe who do dangerous and unappreciated work that is vital and necessary to our wellbeing. Thank your garbage man today!"
)
add_holiday(6, 17,
	"World Tessellation Day",
	"Tesselation, also known as tiling, is the art of covering a flat surface with a repeating pattern of geometric shapes. Today celebrates the geometry-based art form that combines mathematical analysis with creative design. Try out making your own tessellated patterns, or just take the time to appreciate an example of tessellation in your life (like your kitchen tiles)!"
)

add_holiday(6, 18,
	"International Sushi Day",
	"A day for celebrating the traditional Japanese dish that has become beloved worldwide. Eat some sushi today!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/International-Sushi-Day-PB-599721_1920-750x375.jpg"
)
add_holiday(6, 18,
	"National Go Fishing Day",
	"Today is a good opportunity to go fishing, especially if you've never been before and want to try it out!"
)
add_holiday(6, 18,
	"International Picnic Day",
	"Today is also a good opportunity to go on a summer picnic! (Perhaps near a fishing spot?)"
)
add_holiday(6, 18,
	"Clean Your Aquarium Day",
	"If you have an aquarium, make sure it's clean today!"
)

add_holiday(6, 19,
	"Juneteenth",
	"A day celebrating the abolition of slavery in the United States, with the date commemorating the final enforcement of the Emancipation Proclamation in Texas on June 19th, 1865.",
	img="https://nationaltoday.com/wp-content/uploads/2021/06/Juneteenth-1-1200x834.jpg"
)
add_holiday(6, 19,
	"National Garfield the Cat Day",
	"The very first Garfield comic strip debuted on June 19th, 1978. Today fans celebrate the iconic character's birthday."
)
add_holiday(6, 19,
	"National Watch Day",
	"Both a monumental technological invention and a cornerstone of fashion and culture, today is a day to appreciate the humble wristwatch."
)

add_holiday(6, 20,
	"American Eagle Day",
	"Less commonly known as Bald Eagle Appreciation Day, this commemoration was originally established to raise awareness of the endangered status of the bald eagle and the ongoing conservation efforts surrounding it. Today, the bald eagle has thankfully made a full recovery and is considered a Least Concern species. The holiday remains as a celebration of the majestic bird and the importance of its symbolism to Americans, as well as a reminder of the threats to survival that many other animals on our planet are still facing.",
	img="https://www.holidaycalendar.io/images/holiday-images/bald-eagle-appreciation-day/medium.jpg"
)
add_holiday(6, 20,
	"World Refugee Day",
	"Established by the United Nations General Assembly to raise awareness of the struggles faced by refugees worldwide, call for the humane treatment of refugees, and honor the bravery of those who have been forced to flee their countries."
)

add_holiday(6, 21,
	"World Music Day",
	"Also known as Make Music Day, this holiday started as a festival in France in 1982 and blossomed into a worldwide celebration. Today we celebrate music in all its forms and appreciate the impact that it has on our daily lives. Today everyone is encouraged to either make or listen to some music!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/06/Make-Music-Day-PB-445387_1920-750x375.jpg"
)
add_holiday(6, 21,
	"International Day of Yoga",
	"Instated by the United Nations General Assembly in 2015, this holiday seeks to promote the practice of yoga by spreading awareness of its physical and mental health benefits. If you've never tried yoga, take the opportunity today!"
)
add_holiday(6, 21,
	"World Giraffe Day",
	"A day to celebrate and appreciate our planet's tallest living animal. Giraffes are currently considered an endangered species, and this day each year the Giraffe Conservation Foundation holds a fundraising event for their conservation efforts."
)
add_holiday(6, 21,
	"Go Skateboarding Day",
	"A day celebrating the beloved sport of skateboarding, which aims to welcome interested newcomers into the hobby. If you have a skateboard, today is a good day to take it out for a spin!"
)

add_holiday(6, 22,
	"World Rainforest Day",
	"A day to appreciate the rainforest, one of the most diverse ecosystems on our planet and an important element in regulating our climate. The holiday was established to bring awareness to the importance of rainforests and the threats to their survival like deforestation and climate change.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/World-Rainforest-Day-pexels-2739664-750x375.jpg"
)
add_holiday(6, 22,
	"National Onion Ring Day",
	"A day to celebrate the beloved American snack food. Many burger restaurants run onion ring-related promotions today!"
)
add_holiday(6, 22,
	"National Chocolate Eclair Day",
	"A day to celebrate the delicious French dessert pastry. Have a chocolate eclair today!"
)

add_holiday(6, 23,
	"National Hydration Day",
	"Remember to drink water today! This holiday was established in honor of Victor Hawkins, a football coach who invented a new hydrating mouthguard for his players, and serves as a reminder of the importance of hydration.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/12/National-Hydration-Day-750x375.jpg"
)
add_holiday(6, 23,
	"National Typewriter Day",
	"A day to appreciate the monumental technological invention of the typewriter, as well as the freedom of expression that it represents. Today would be a good day to visit a typewriter museum or try out a publicly-available typewriter, but it's also a good excuse to do some work on a personal writing project, even if it's not on a typewriter."
)
add_holiday(6, 23,
	"International Women in Engineering Day",
	"A day to honor all of the women who have made important technological contributions (such as Ada Lovelace, Stephanie Kwolek, Katherine Johnson, and many, many more), as well as all of the women who currently work in the field of engineering."
)

add_holiday(6, 24,
	"St. John's Day",
	"This Christian feast day commemorating the birthday of St. John the Baptist has become a popular holiday in many different countries around the world, with many of the celebrations having diverged from the Christian origins and transformed into secular traditions of family gatherings, public festivals, and more. In Quebec, the day is called St. Jean-Baptiste Day; in Venezuela, it's Fiesta De San Juan; in Brazil, it's Festa Junina (or Festa de São João); etc.",
	img="https://nationaltoday.com/wp-content/uploads/2020/06/Saint-Jean-Baptiste-1200x834.jpg"
)
add_holiday(6, 24,
	"National Upcycling Day",
	"In contrast to recycling, upcycling is the process of directly repurposing a waste item as something new and useful; for example, plastic bottles and tin cans can be reused as planters if properly prepared. The holiday was created to encourage the practice of upcycling in everyday life to reduce the amount of personal waste created. If you've never tried upcycling before, today is a good opportunity to try it out!"
)
add_holiday(6, 24,
	"National Pralines Day",
	"A day to celebrate the iconic Southern dessert confection made from pecans and sugar. Eat some pralines today!"
)

add_holiday(6, 25,
	"Leon Day",
	"Leon Day (which gets its name from \"Noel\" spelled backwards) marks the halfway point to Christmas, and for hardcore Christmas fans it's an excuse to hold a halfway-to-Christmas celebration. If you've been missing your favorite Christmas traditions like watching Christmas movies or listening to Christmas music, today is your opportunity to indulge yourself in a little bit of Christmas spirit. (This holiday is similar to, but distinct from, Christmas in July, which takes place a month from now!)",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/03/National-Leon-Day-iStock-1019842702-750x375.jpg"
)
add_holiday(6, 25,
	"Global Beatles Day",
	"A day to appreciate the music of the Beatles and celebrate the monumental contributions that they made to the history of pop music. The date symbolizes the global unifying power of the Beatles' music - it commemorates the first ever globally-broadcast live television event, a live performance of the song *All You Need is Love*, broadcast on June 25th, 1967. Listen to some music from the Beatles today!"
)
add_holiday(6, 25,
	"National Catfish Day",
	"This holiday was established in 1987 by President Ronald Reagan to promote America's then-growing catfish farming industry. Today, it's just a good opportunity to eat some delicious Southern seafood."
)

add_holiday(6, 26,
	"National Canoe Day",
	"A primarily Canadian holiday that celebrates the hobby and sport of canoeing as well as the historical and cultural importance of the canoe. Many boating enthusiasts celebrate the day by attending canoe river tours, canoe races, and more.",
	img="https://nationaltoday.com/wp-content/uploads/2022/05/82-Canoe-Day-1200x834.jpg.webp"
)
add_holiday(6, 26,
	"World Refrigeration Day",
	"A day to appreciate the monumental technological invention of in-home mechanical refrigeration and the impact that it's had on our daily lives."
)
add_holiday(6, 26,
	"National Chocolate Pudding Day",
	"Eat some chocolate pudding today!"
)

'''
6/27
'''

'''
6/28
'''

add_holiday(6, 29,
	"International Day of the Tropics",
	"A day established by the United Nations to raise awareness of the environmental threats faced by the tropics, the region of ecosystems surrounding the planet's equator.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/09/International-Day-Of-The-Tropics-PB-273780_1920-750x375.jpg"
)
add_holiday(6, 29,
	"National Camera Day",
	"A day celebrating the monumental technological invention of the camera and the cultural importance of photography. Celebrate the day by taking a picture or two!"
)
add_holiday(6, 29,
	"National Waffle Iron Day",
	"A day to appreciate the invention of the waffle iron. Just imagine how much more difficult it would be to make waffles without them!"
)

add_holiday(6, 30,
	"International Asteroid Day",
	"Founded by a group including physicist Stephen Hawking, astronaut Rusty Schweickart, and astrophysicist/guitarist Brian May, and sanctioned by the United Nations, this event aims to raise awareness about the threat of meteor impacts on our planet and encourages global protections to prepare for such an event. The date was chosen to commemorate the Tunguska event, when a meteor impact leveled a section of a Siberian forest on June 30th, 1908.",
	img="https://www.almanac.com/sites/default/files/images/interstellar-meteor.jpg"
)
add_holiday(6, 30,
	"National Meteor Watch Day",
	"Coinciding with International Asteroid Day, this holiday celebrates the more fun and innocent aspects of meteor interactions with our planet with an event dedicated to the activity of meteor watching. Look for shooting stars tonight!"
)




add_holiday(7, 1,
	"American Zoo Day",
	"A day celebrating the importance of zoos and the contributions they make to animal conservation and public education. The date commemorates the opening of the first zoo in the United States, the Philadelphia Zoo, on July 1st, 1874. Visit your local zoo today!",
	img="https://nationaltoday.com/wp-content/uploads/2021/06/American-Zoo-Day-1200x834.jpg"
)
add_holiday(7, 1,
	"Canada Day",
	"Also known as Fête du Canada or \"Canada's Birthday,\", today commemorates Canada's establishment on July 1st, 1867 and is a federal holiday there."
)
add_holiday(7, 1,
	"Second Half of the Year Day",
	"The first day of the seventh month in the year means that the year is just about halfway over!"
)

add_holiday(7, 2,
	"World UFO Day",
	"A day celebrating our continual fascination with the concept of UFOs and alien encounters. The date commemorates the Roswell Incident, a supposed UFO crash landing in Roswell, New Mexico on July 2nd, 1947. Celebrate the day by watching a movie about aliens, or even visiting a UFO destination like Roswell if you live near one!",
	img="https://nationaltoday.com/wp-content/uploads/2020/07/World-UFO-1200x834.jpg"
)
add_holiday(7, 2,
	"National I Forgot Day",
	"Um... I can't quite remember what this holiday's about..."
)

add_holiday(7, 3,
	"National Stay Out of the Sun Day",
	"Although regular exposure to sunlight is necessary for a healthy lifestyle, this holiday exists to serve as a reminder of the potential downsides of too much sun (such as skin damage and even cancer), especially during the summer months when people are most likely to be out in bright sunlight. If you are going to be outdoors today, make sure you take precautions like wearing sunscreen and staying in the shade whenever possible.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/National-Stay-Out-Of-The-Sun-Day-PB-4047678_1920-750x375.jpg"
)
add_holiday(7, 3,
	"Air Conditioning Appreciation Day",
	"A day honoring the incredible comfort and convenience that air conditioning contributes to our everyday lives. It's great that this event coincides with National Stay Out of the Sun Day - it's a good opportunity to stay indoors and let your air conditioner do its work today!"
)

add_holiday(7, 4,
	"Independence Day",
	"Also known as the Fourth of July, today commemorates the establishment of the United States of America on July 4th, 1776. Grill up some classic American food and watch some fireworks today!",
	img="https://nationaltoday.com/wp-content/uploads/2020/07/4july-1-1200x834.jpg"
)
add_holiday(7, 4,
	"Alice in Wonderland Day",
	"Most commonly celebrated in England, this event commemorates the day when the story that would eventually become *Alice's Adventures in Wonderland* was first told by Lewis Carroll on July 4th, 1862. The day celebrates Carroll's classic literary works and their massive cultural impact."
)

add_holiday(7, 5,
	"Pet Remembrance Day",
	"A United Kingdom holiday that honors all of the beloved animal companions in our lives who have passed away.",
	img="https://upload.wikimedia.org/wikipedia/commons/6/61/20110425_German_Shepherd_Dog_8505.jpg"
)
add_holiday(7, 5,
	"National Apple Turnover Day",
	"Eat an apple turnover today!"
)

add_holiday(7, 6,
	"National Fried Chicken Day",
	"A day celebrating American fried chicken, a popular soul food dish. Fried chicken arose from the combining of Scottish frying techniques and West African seasoning techniques in the American South, where it originally became popular because it kept well without refrigeration compared to other preparations of chicken. Celebrate by eating some fried chicken today!",
	img="https://nationaltoday.com/wp-content/uploads/2019/07/national-fried-chicken-day-1200x834.jpg.webp"
)

add_holiday(7, 7,
	"World Chocolate Day",
	"A global celebration of chocolate, the beloved confection originating in Mesoamerica. Chocolate is made by mixing cocoa with just sugar (dark chocolate) or sugar and milk (milk chocolate). The date of the event supposedly commemorates the first import of chocolate to Europe, which is rumored to have taken place on July 7th, 1550. Celebrate the day by eating some chocolate or something made with chocolate! (American chocolate lovers have more to look forward to later in the year - October 28th is National Chocolate Day in the USA.)",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/06/World-Chocolate-Day-pexels-8105105-750x375.jpg"
)
add_holiday(7, 7,
	"National Koi Day",
	"A day celebrating the Japanese Koi fish, a beautiful variety of carp which is kept worldwide. The date honors Hanako, the world's oldest Koi fish, who lived for 226 years before her death on July 7th, 1977."
)
add_holiday(7, 7,
	"International Peace & Love Day",
	"Today is the birthday of Ringo Starr (of the Beatles), which fans celebrate with an event named after his iconic catchphrase. The day was started in 2008, when an interviewer asked Ringo what he wanted for his birthday, and he simply responded, \"peace and love.\" Since then, the event has been a yearly celebration of the hopes and ideals expressed in the 60's-originating phrase."
)

add_holiday(7, 8,
	"Be a Kid Again Day",
	"This event simply encourages everyone to participate in an activity that they enjoyed at a younger age but haven't done in recent years. Take the opportunity today to enjoy a movie you used to watch as a kid, play a game you used to play as a kid, etc.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/11/Video-Games-Day-750x375.jpg"
)
add_holiday(7, 8,
	"National Freezer Pop Day",
	"A day celebrating the freezer pop, a humble yet beloved summery dessert."
)
add_holiday(7, 8,
	"National Blueberry Day",
	"A day celebrating blueberries, right in the middle of their summer harvest months."
)
'''
add_holiday(7, 8,
	"National Video Game Day [[[PLACEHOLDER]]]",
	""
)

Ice Cream Sundae Day ???

'''

add_holiday(7, 9,
	"National Sugar Cookie Day",
	"A day celebrating the simple but classic American-originating cookie. Try making some sugar cookies today, or just enjoy some store-bought ones!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/11/National-Sugar-Cookie-Day-750x375.jpg"
)
add_holiday(7, 9,
	"Fashion Day",
	"A day dedicated to the widespread hobby/interest of fashion."
)

add_holiday(7, 10,
	"National Piña Colada Day",
	"A day celebrating the iconic tropical cocktail that was invented to embody the taste of the islands. Made with a mixture of rum, pineapple juice, and coconut cream, this drink was invented in Puerto Rico in 1954 and has become a classic icon in the years since.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/09/National-Pina-Colada-Day-750x375.jpg"
)
add_holiday(7, 10,
	"National Kitten Day",
	"This holiday was originally created to encourage the adoption of homeless kittens, but even if you're not up for adopting a new feline friend today, the event is a good opportunity to celebrate the joy that cats bring to our lives. Pet your cat if you have one, watch some kitten videos on YouTube, etc."
)
add_holiday(7, 10,
	"Pick Blueberries Day",
	"We just had National Blueberry Day on July 8th, but today specifically celebrates the fun summer activity of blueberry picking. Grab a basket and go pick some berries today!"
)

add_holiday(7, 11,
	"National 7-Eleven Day",
	"Also known as National Free Slurpee Day, today is celebrated by the American gas station chain as a play on the date (7/11). Today all 7-Eleven locations give out free Slurpees (their brand of slushy drink) to customers. Go get a free Slurpee today!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2022/03/National-7-Eleven-Day-750x375.jpg"
)
add_holiday(7, 11,
	"National Swimming Pool Day",
	"This simple holiday celebrates the activity of going swimming in the summer months. Stop by a swimming pool today!"
)
add_holiday(7, 11,
	"National State Fair Food Day",
	"A day to celebrate all of the wacky but iconic foods known for being served at state fairs, such as various deep-fried candies and cookies, funnel cake, corn dogs, cotton candy, kettle corn, churros, cheese curds, and more."
)
add_holiday(7, 11,
	"World Population Day",
	"This event commemorates July 11th, 1987, the estimated date when the world's population reached 5 billion people. It was established by the United Nations to bring awareness to the issues of overpopulation as our population continues to grow rapidly."
)

add_holiday(7, 12,
	"National Simplicity Day",
	"A day commemorating the birthday of Henry David Thoreau, born on July 12th, 1817. Thoreau was a naturalist, transcendentalist, and proto-anarchist, as well as a proponent of the practice of simple living. Today celebrates the simple living philosophy and encourages us all to appreciate the simple joys in life.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/03/National-Simplicity-Day-750x375.jpg"
)
add_holiday(7, 12,
	"National Different Colored Eyes Day",
	"A day celebrating and appreciating all those who have heterochromia (eyes with two differently-colored pupils)."
)
add_holiday(7, 12,
	"National Pecan Pie Day",
	"Eat a pecan pie today!"
)

add_holiday(7, 13,
	"National Rock Day",
	"A day to celebrate the subject of geology. Take the time today to appreciate your favorite rocks!",
	img="https://nationaltoday.com/wp-content/uploads/2022/07/lkjhgfhjkl-6-min-1200x834.jpg.webp"
)
add_holiday(7, 13,
	"Gruntled Workers Day",
	"A special day for those who are actually quite satisfied with their jobs."
)

add_holiday(7, 14,
	"International Non-Binary Peoples Day",
	"A day to celebrate nonbinary peoples and raise awareness of the societal issues that they continue to face. Additionally, coinciding with the holiday, Non-Binary Awareness Week is taking place from Monday to Sunday this week. As a fun fact, the date was chosen as the halfway point in the year between International Women's Day (March 8th) and International Men's Day (November 19th).",
	img="https://nationaltoday.com/wp-content/uploads/2022/09/4568339-min-1200x834.jpg.webp"
)
add_holiday(7, 14,
	"Bastille Day",
	"Also called La Fête Nationale and \"le 14 juillet\" in France, today celebrates the French Revolution and the liberation of the French people from tyranny. The date commemorates the storming of the Bastille, a political prison in Paris, on July 14th, 1789; this event is often considered the beginning of the Revolution. This event has been a major national holiday in France since the very first anniversary of the storming in 1790."
)
add_holiday(7, 14,
	"Shark Awareness Day",
	"A day raising awareness of sharks, their importance to our ecosystems, and the manmade endangerment that they face. Take the time to appreciate sharks today by watching a shark documentary, reading a book on sharks, etc. "
)
add_holiday(7, 14,
	"National Mac & Cheese Day",
	"Eat some mac & cheese today!"
)
'''
NATIONAL CHIMPANZEE DAY 7/14 !!!
'''

add_holiday(7, 15,
	"National I Love Horses Day",
	"A day celebrating the relationship between humanity and horses and the historical importance of horses to our society. Celebrate by going horse riding, watching a horse race, or just taking time to appreciate horses! (Horse lovers have more to look forward to on December 13th, which is National Horse Day.)",
	img="https://www.holidayscalendar.com/wp-content/uploads/2022/03/National-I-Love-Horses-Day-750x375.jpg"
)
add_holiday(7, 15,
	"National Orange Chicken Day",
	"Inspired by a Hunan dish called Chen Pi Ji (tangerine chicken), orange chicken is an American-Chinese style of fried chicken prepared with a sweet orange chili sauce. The holiday was established in 2017 by Panda Express, a chain restaurant closely associated with the popularity of orange chicken, to promote the dish to American audiences."
)
add_holiday(7, 15,
	"Gummi Worm Day",
	"A day to celebrate the gummi worm, an alternative to gummi bears created by German company Trolli which supposedly debuted on July 15th, 1981. Eat some gummi worms today!"
)

add_holiday(7, 16,
	"Guinea Pig Appreciation Day",
	"A day celebrating guinea pigs. These animals originate from the South American Andes and were originally domesticated as livestock, but are now mostly kept as pets. They were also historically common animal test subjects in laboratory experiments. Today aims to honor all of the contributions that guinea pigs have made to our lives, especially the furry friends kept as animal companions.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/Guinea-Pig-Appreciation-Day-PB-242520_1920-750x375.jpg"
)
add_holiday(7, 16,
	"World Snake Day",
	"Another pet-centric day, this event honors snakes and encourages a more positive cultural perception of the fascinating creatures."
)
add_holiday(7, 16,
	"National Cherry Day",
	"A day celebrating all forms of cherries, from fresh black cherries to maraschino cherries to sweet foods made from cherries. Eat some cherries today!"
)

add_holiday(7, 17,
	"World Emoji Day",
	"Apple originally designed their calendar emojis with the date July 17th as a reference to the unveiling of the iCal app on July 17th, 2002, and since then the majority of emoji systems use the date, too. Even Discord, which uses the Twemoji design set, shows this date: :date: Emoji enthusiasts have celebrated the date as World Emoji Day since 2014. The event's official website can be found [here](<https://worldemojiday.com/>).",
	img="https://nationaltoday.com/wp-content/uploads/2020/07/World-Emoji--1200x834.jpg"
)
add_holiday(7, 17,
	"Yellow Pigs Day",
	"This holiday is most closely associated with Hampshire College in Amherst, Massachusetts, where mathematicians celebrate the prime number 17 and all of its unique properties each year on 7/17. The event was founded by mathematicians David Kelly and Michael Spivak, and each year alumni of Kelly's mathematics program gather on campus to eat yellow pig cake, sing yellow pig carols, and attend a lecture by Kelly on the number 17. The event is most popular in Amherst, but mathematicians everywhere have begun celebrating the holiday by making and wearing yellow pig shirts, eating yellow pig cakes, etc., as well as studying the number 17. (There's a lot of misinformation floating around about Yellow Pigs Day; check out [this link](<https://hcssim.org/yellow-pigs-day/>) for a trustworthy source.)"
)
add_holiday(7, 17,
	"Wrong Way Corrigan Day",
	"On July 17th, 1938, after having his request to fly solo from New York to Dublin denied by air traffic officials, Douglas Corrigan made the 28-hour journey anyway, claiming upon landing that he accidentally went the wrong way after taking off. His stunt made him a contemporary celebrity (even leading to a biographical movie starring himself the following year), and his flight is commemorated in both Long Island and his hometown of Galveston, Texas as Wrong Way Corrigan Day."
)
add_holiday(7, 17,
	"National Tattoo Day",
	"A day to honor the artistry and cultural significance of tattoos. If you've got a tattoo, show it off today!"
)

add_holiday(7, 18,
	"Nelson Mandela Day",
	"Today commemorates Nelson Mandela's birthday (July 18th, 1918) and honors his life and achievements. Mandela spent 27 years imprisoned for his anti-Apartheid activism and sabotage campaign against the Apartheid government. He served as South Africa's first president, and the country's first black head of state, from 1994 to 1999. He passed away in 2013, but is revered in South Africa as the \"Father of the Nation\" and celebrated globally as a role model of anti-racism.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/Nelson-Mandela-Day-iStock-460843347-750x375.jpg"
)
add_holiday(7, 18,
	"National Caviar Day",
	"A day celebrating caviar, a delicacy consisting of salt-cured roe (fish eggs). The most accessible type is \"substitute\" caviar made from salmon roe, but \"true\" caviar comes from sturgeon fish in the Caspian Sea and Black Sea. Caviar fans, take the opportunity to enjoy some caviar today!"
)
add_holiday(7, 18,
	"National Sour Candy Day",
	"A day celebrating sour candy in all its forms, from small tarts to sour straws to children-shaped gummies. Enjoy your favorite sour candy today!"
)

add_holiday(7, 19,
	"National Daiquiri Day",
	"A day dedicated to the daiquiri, an alcoholic drink made with rum, fruit juice, and sweetener. The beverage is named after the small Cuban mining village of Daiquiri, where it was invented, and is now closely associated with the city of Havana.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/09/National-Daiquiri-Day-750x375.jpg"
)
add_holiday(7, 19,
	"National Football Day",
	"A day celebrating the beloved sport of American football. Celebrate by watching a football game today!"
)

add_holiday(7, 20,
	"Space Exploration Day",
	"Declared as Space Exploration Day by President Ronald Reagan in 1984 and International Moon Day by the United Nations in 2021, today commemorates the first crewed moon landing on July 20th, 1969, when Neil Armstrong and Buzz Aldrin (aided by Michael Collins) of the Apollo 11 mission became the first human beings to walk on the moon. The holiday aims to keep public interest in space exploration alive (in spite of difficulties faced by NASA and other space exploration programs) by reminding us all of magical moments like the moon landing.",
	img="https://upload.wikimedia.org/wikipedia/commons/9/98/Aldrin_Apollo_11_original.jpg"
)
add_holiday(7, 20,
	"International Chess Day",
	"Established by UNESCO in 2019, today celebrates the widely beloved game of chess. Take the opportunity today to play a chess game, or even watch a high-level game between professional players."
)
add_holiday(7, 20,
	"National Fortune Cookie Day",
	"A day celebrating the fortune cookie, a novelty dessert item served in many American-Chinese restaurants. The modern fortune cookie was inspired by tsujiura senbei, a folded cookie that contained a fortune inside, which originated in Kyoto, Japan in the 1800s (and was itself inspired by omikuji, a \"fortune lottery\" tradition in Shinto temples). The first modern fortune cookies were invented by Japanese immigrants to America and became extremely popular with Chinese restaurants. Have a fortune cookie today!"
)
add_holiday(7, 20,
	"National Lollipop Day",
	"Enjoy a lollipop today!"
)

add_holiday(7, 21,
	"National Junk Food Day",
	"A day celebrating all the different kinds of foods that are high in fats, sugars, sodium, and/or calories, or are otherwise bad for your body, but still taste delicious. Most days of the year, these types of foods should generally be avoided and only occasionally enjoyed as a special treat, but today is all about the simple hedonistic pleasure of deliciously terrible food.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/11/National-Junk-Food-Day-750x375.jpg"
)

add_holiday(7, 22,
	"Pi Approximation Day",
	"A sister holiday to Pi Day (3/14), July 22nd is Pi Approximation Day because its date (formatted as 22/7 in some countries) matches the fraction 22/7, a common close approximation for the value of pi. Celebrate today by studying the mathematical significance of the number pi and its approximations, or just have some pie!",
	img="https://nationaltoday.com/wp-content/uploads/2022/05/26-Pi-Day-1200x834.jpg.webp"
)
add_holiday(7, 22,
	"National Mango Day",
	"A day celebrating the mango, a fruit native to India and associated with tropical climates and summery weather. Celebrate the day by enjoying some mango or your favorite food item made from mango!"
)
add_holiday(7, 22,
	"National Hammock Day",
	"A day where hammock owners are encouraged to enjoy some rest and relaxation in their hammocks."
)

add_holiday(7, 23,
	"National Vanilla Ice Cream Day",
	"Though vanilla ice cream is often considered the \"default\" flavor or even treated as a flavorless base for more complex desserts, vanilla is its own complex and nuanced flavor that was considered an exotic delicacy for many years, and the ice cream made from it can stand on its own next to chocolate and other iconic flavors. Today is a holiday dedicated to appreciating the often-dismissed vanilla ice cream; celebrate by enjoying some, whether on its own or prepared with your favorite toppings.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2020/09/National-Vanilla-Ice-Cream-Day-750x375.jpg"
)
add_holiday(7, 23,
	"National Sprinkle Day",
	"A day celebrating the humble sprinkles, tiny bits of candy used to top larger desserts for both aesthetic and texture, also known as jimmies, vermicelli, hundreds and thousands, hagelslag, shots, and more. Celebrate today with some sprinkles on top of your dessert of choice (perhaps some vanilla ice cream)!"
)

add_holiday(7, 24,
	"National Tequila Day",
	"A day celebrating tequila, a spirit distilled from the juice of the blue agave plant. Tequila is named after the Mexican city of Santiago de Tequila, Jalisco, and is the national drink of Mexico. The drink is considered culturally important enough that international agreements legally prohibit any alcohol produced outside of Mexico from being labeled as tequila.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/National-Tequila-Day-iStock-987369206-750x375.jpg"
)
add_holiday(7, 24,
	"Amelia Earhart Day",
	"Today commemorates the birthday of Amelia Earhart, born on July 24th, 1897. She was a pioneer of aviation and a celebrity pilot, and she set many world records in her life, most notably as the first female pilot to successfully fly solo non-stop across the Atlantic Ocean. She was also an inspirational figure in women's rights who worked alongside Eleanor Roosevelt to advocate for women's causes, as well as an accomplished author with successful autobiographical writings about her own achievements. She disappeared on July 2nd, 1937, during an attempted non-stop flight across the Pacific Ocean, a tragic loss that cemented her status as a legendary figure in American history."
)

add_holiday(7, 25,
	"Christmas in July",
	"In the United States and the rest of the Northern Hemisphere, Christmas in July is a deliberately ironic and comedic event that blends the wintery celebration of Christmas with the mid-summer month of July; the concept first gained popularity in the 1940s and 1950s. However, in many Southern Hemisphere countries, Christmas in July actually serves the purpose of letting people hold Christmas celebrations during the winter (whereas December 25th falls at the beginning of summer). Many stores hold sales today (either for Christmas decorations or just general promotions), and the Hallmark Channel runs a Christmas in July marathon around this time of year.",
	img="https://upload.wikimedia.org/wikipedia/commons/1/13/Christmas_in_july_au.jpg"
)
add_holiday(7, 25,
	"Carousel Day",
	"Also known as National Merry-Go-Round Day, this event celebrates the classic amusement ride consisting of seats supported by a rotating platform, often decorated as galloping horses and racing chariots. The ride has history dating back to the 1600s; some of the earlier versions were pulled by actual ponies before a steam-powered version was invented in 1861. This event was established by the National Carousel Association, an organization of enthusiasts who work for the preservation of classic carousel rides."
)
add_holiday(7, 25,
	"Culinarians Day",
	"A day honoring chefs, cooks, and culinary professionals. Celebrate today by taking time to cook one of your meals from scratch, or, if you go out to a restaurant, be sure to thank the chef!"
)
add_holiday(7, 25,
	"National Wine and Cheese Day",
	"A day celebrating the popular pairing of wine and cheese. Celebrate today by enjoying this classic combination!"
)

add_holiday(7, 26,
	"National Dog Photography Day",
	"A holiday as simple as it is fun, this event is simply a chance to take photos of your dog and share them with others. You could even post some dog pictures in this very Discord server!",
	img="https://nationaltoday.com/wp-content/uploads/2022/06/25-Dog-Photo-1200x834.jpg.webp"
)
add_holiday(7, 26,
	"National Aunt and Uncle Day",
	"Similar to the more popular Mother's Day and Father's Day, this event honors our uncles and aunts and the roles that they play in our lives. If you have any aunts or uncles you appreciate, let them know today!"
)
add_holiday(7, 26,
	"World Tofu Day",
	"A day celebrating tofu, a protein food item made from soybeans which originated in China over 2,000 years ago. Though it's mostly used in Western cooking as a plant-based substitute for meat, tofu is a traditional component of Asian cuisine and can be easily enjoyed on its own merits. Have some tofu today!"
)

add_holiday(7, 27,
	"National Chicken Finger Day",
	"A day dedicated to chicken fingers (also known as chicken tenders and chicken strips), a preparation of breaded and fried chicken first invented in Manchester, New Hampshire in 1974. This event was established by Louisiana-originating fast food chicken finger chain Raising Cane's in 2010. Raising Cane's usually runs promotional events today, but you can celebrate by visiting any of your favorite restaurants that serve tendies, or make your own!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/07/National-Chicken-Finger-Day-pexels-60616-750x375.jpg"
)
add_holiday(7, 27,
	"National Crème Brûlée Day",
	"Translated simply as \"burnt cream,\" crème brûlée is a dessert consisting of rich custard with a top that has been burnt to form a layer of hardened caramelized sugar. This dish originated in medieval-era Spain and later became popularized by fine French restaurants in the 1980s. Have some crème brûlée today!"
)

add_holiday(7, 28,
	"National Waterpark Day",
	"A day celebrating and honoring the waterpark, the underappreciated cousin of the traditional amusement park. Waterparks are a type of amusement park featuring water-based attractions like swimming pools, wave pools, lazy rivers, water slides, water coasters, water playgrounds, and more. They operate seasonally during summer months in the outdoors or year-round indoors, and are sometimes built as a second gate to larger amusement parks. Though less popular than the generic amusement park, waterparks still have their own fascinating history and lots of attractions to offer, and are a great destination during these hot summer months!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/09/National-Waterpark-Day-750x375.jpg"
)
add_holiday(7, 28,
	"National Soccer Day",
	"A day celebrating the sport of soccer (known outside the USA as football), currently the most popular sport globally. Soccer has a long history beginning with ancient ball-kicking games and particularly games played in medieval England, while the modern sport is thought to have been first unified with the establishment of the Football Association in 1863. With so many games being played around the world each day, today is a good day to watch a soccer game!"
)
add_holiday(7, 28,
	"World Nature Conservation Day",
	"Established in India but celebrated worldwide, this event celebrates the beauty of our natural world and calls for the conservation of our planet's natural ecosystems in face of the manmade threats to their existence."
)

add_holiday(7, 29,
	"International Tiger Day",
	"A day honoring the tiger, a fascinating species of big cat native to Asia. Tigers have been important to our culture since antiquity, from representation in local mythologies and folklore to featuring heavily in circus acts historically to acting as animal ambassadors for environmental causes in the modern day. Tigers are officially considered endangered, and it's estimated that under 6,000 individuals live in the wild; this event acts as a call to support conservation efforts for these incredibly significant and important animals.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/06/International-Tiger-Day-pexels-2541239-750x375.jpg"
)
add_holiday(7, 29,
	"National Chicken Wing Day",
	"Chicken wings have been eaten since the beginning of people eating chickens, but in modern times, wings were considered an undesirable part of the chicken until Buffalo wings were invented in Buffalo, New York, in the year 1964. After Buffalo wings experienced a nationwide explosion in popularity, leading to wide acceptance of many different preparations of chicken wings in general, the city of Buffalo established National Chicken Wing Day in 1977. Many restaurants (including Buffalo Wild Wings, Wingstop, Popeye's, and more) run promotional deals on wings today, so it's a great opportunity to enjoy some chicken wings!"
)
add_holiday(7, 29,
	"National Lasagna Day",
	"A day celebrating lasagna, a traditional type of pasta originating in medieval Italy, prepared by stacking flat sheets of pasta in alternating layers with fillings such as meat sauce, cheese, and vegetables. Have some lasagna today!"
)
add_holiday(7, 29,
	"Rain Day",
	"A celebration closely associated with the city of Waynesburg, Pennsylvania, where a Rain Day festival is held each year. In 1874, after a neighbor noticed that it often rained on July 29th, local pharmacist William Allison began noting out of curiosity whether or not it rained on that day each year. After William died, the recordkeeping was continued by his brother Albert, and then later continued by a succession of Waynesburg residents. In 1979, the Rain Day festival was established by the city, and interest in the recordkeeping began spreading to other locales. In 1985, the celebration was brought popularity when it was featured on NBC by Willard Scott the Weatherman (of Ronald McDonald fame). As of 2024, it has rained on 7/29 in Waynesburg 118 times out of the past 151 years; will it rain again this year?"
)



'''
7/30 - 8/7
'''



add_holiday(8, 8,
	"International Cat Day",
	"A day to raise awareness for cats, and learn about ways to help/protect them. This holiday was started in 2002 by the International Fund for Animal Welfare (in Canada), but has since been passed to International Cat Care, a British nonprofit that has been working to improve the health/welfare of domestic cats since 1958. Many countries have their own \"National Cat Day\" as well (such as Japan’s on February 22nd, which predates the international counterpart), though Canada uniquely has their National Cat Day on August 8th, too (since the holiday was founded by a Canadian organization).",
	img="https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg"
)
add_holiday(8, 8,
	"Happiness Happens Day",
	"Formerly known as \"Admit You’re Happy Day\", this holiday was created by the Secret Society of Happy People (SOHP) in 1999 to celebrate their first anniversary as an organization. The following year, they also declared August as Happiness Happens Month. The purpose of this day/month is to share happiness and encourage people to talk and think about happiness in their lives. Additionally, the organization runs a yearly online event around Happiness Happens Day called \"HappyThon,\" aiming to promote happiness around the world through social media."
)
add_holiday(8, 8,
	"National Mochi Day",
	"A day celebrating mochi, a type of rounded rice cake (often sweetened) originating in Japan. There are many variants of mochi, including the ice cream mochi popular in the USA. Mochi is as old as Japanese cultivation of rice, having been invented sometime before 300 BCE; it's a culturally significant dish in Japan and is a traditional food eaten during New Year celebrations. Celebrate by enjoying your favorite kind of mochi today!"
)

add_holiday(8, 9,
	"National Book Lovers Day",
	"A day that aims to celebrate the timeless and beloved art form of literature as well as encourage more people to take up reading. Take the opportunity to read a book today!",
	img="https://nationaltoday.com/wp-content/uploads/2020/08/Book-Lovers-1-1200x834.jpg"
)
add_holiday(8, 9,
	"International Day of the World’s Indigenous People",
	"Established by the United Nations in 1994, this event honors all those worldwide who belong to indigenous peoples and first nations, and advocates for awareness and protection of global indigenous rights."
)

'''
8/10 - 8/11
'''

add_holiday(8, 12,
	"National Vinyl Record Day",
	"A day celebrating the vinyl record, the first truly popular medium for audio recording storage. The invention of long-play records had a revolutionary impact on the music industry and directly led to the dominance of the album format in popular music. These days, vinyl records still stand alongside newer physical formats like CDs in terms of popularity because of their superior audio quality and collector's value. Celebrate today by listening to a record, or maybe visiting your local record store!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2021/03/vinyl-record-day-2254165-PB-750x375.jpg"
)
add_holiday(8, 12,
	"Middle Child Day",
	"A day honoring every middle child, defined as a sibling who is neither the oldest nor youngest within their family unit. Middle children are stereotypically considered to be \"left behind\" compared to the oldest and youngest children, so today is an occasion for celebrating every middle child and giving them the special attention they deserve."
)
add_holiday(8, 12,
	"World Elephant Day",
	"A day celebrating the elephant, mammals native to Africa and Asia who are known for their advanced intelligence, and are the largest living land animal on our planet. Elephants are a primary victim of poaching because of the valuable ivory in their tusks, and all three living species are considered endangered; this event aims to raise awareness of the existential threats to elephants and call for their protection."
)

add_holiday(8, 13,
	"International Left-Handers Day",
	"A day honoring all left-handed people! This event was originally established to bring attention to the special classroom needs and accomodations for left-handed children in a society where most young students are assumed to be right-handed. Today also celebrates left-handed people of all ages and honors the uniqueness of left-handedness.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2023/09/International-Left-Handers-Day-pexels-7951174-750x375.jpg"
)

'''
8/14-8/19
'''



add_holiday(9, 12,
	"National Video Games Day [[[PLACEHOLDER]]]",
	"",
	img=""
)



add_holiday(10, 28,
	"National Chocolate Day [[[PLACEHOLDER]]]",
	""
)

add_holiday(10, 31,
	"Halloween",
	"Short for All Hallows' Eve, this holiday has roots in Celtic Pagan harvest festivals like Samhain and the Western Christian observance of Allhallowtide, but today it is a celebration of the macabre, supernatural, and spooky!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/Halloween-iStock-184596890-750x375.jpg"
)



add_holiday(11, 1,
	"All Saints' Day",
	"A Christian feast day celebrating all saints and martyrs, known and unknown.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/12/All-Saints-Day-iStock-1350932047-750x375.jpg"
)



add_holiday(11, 11,
	"Veterans Day",
	"A day honoring the military veterans of the United States Armed Forces. Originally called Armistice Day, today also commemorates the cessation of hostilities in World War I on November 11th, 1918.",
	img="https://nationaltoday.com/wp-content/uploads/2019/11/veterans-day-1200x834.jpg.webp"
)



add_holiday(12, 13,
	"National Horse Day [[[PLACEHOLDER]]]",
	""
)

add_holiday(12, 24,
	"Christmas Eve",
	"Because of the tradition of the new liturgical day starting at sunset, Christmas Eve has been a part of the Christmas celebration since the holiday was established. The day is celebrated in many different ways, including family gatherings, traditional dinners, caroling, and gift exchanges.",
	img="https://upload.wikimedia.org/wikipedia/commons/6/68/ChristmasEve1878.jpg"
)

add_holiday(12, 25,
	"Christmas",
	"Christmas means many different things to different people. It has roots in Pagan winter solstice celebrations like Yule and Saturnalia, and commemorates the Christian Nativity and the beginning of the Twelve Days of the Christmastide season. In modern times, it celebrates one's family and friends through traditions like gift-giving, family gatherings, feast meals, or even Chinese food and a cinema visit. No matter how you celebrate, have a Merry Christmas!",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/Christmas-iStock-1187452612-750x375.jpg"
)

add_holiday(12, 26,
	"the first day of Kwanzaa",
	"A week-long celebration from December 26th to January 1st, Kwanzaa was created in 1966 as an alternative to the Christmas holiday for African-Americans, but is today celebrated globally to honor all African heritage and culture. Based on traditional African first harvest festivities, Kwanzaa uses its seven days and Seven Symbols to honor its Seven Principles: Unity, Self-Determination, Collective Work and Responsibility, Cooperative Economics, Purpose, Creativity, and Faith.",
	img="https://www.holidayscalendar.com/wp-content/uploads/2016/11/Kwanzaa-iStock-1190087300-750x375.jpg"
)

add_holiday(12, 31,
	"New Year's Eve",
	"The final day of the calendar year, today is a celebration of renewal as the troubles of the past year give way to the fresh opportunities of the coming year. Watch some fireworks and ring in the new year at midnight!",
	img="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Fireworks_on_New_Year%27s_Eve_in_a_small_Swabian_village_%281%29%2C_brightened.jpg/1920px-Fireworks_on_New_Year%27s_Eve_in_a_small_Swabian_village_%281%29%2C_brightened.jpg"
)

add_holiday(12, 31,
	"Karamu",
	"Held on the sixth and penultimate day of the Kwanzaa season, Karamu Ya Imani is a \"feast of faith\" and occasion of communal gathering for those who observe Kwanzaa."
)

# -------- #

print("> Holiday data established")
#print(HOLIDAYS)
