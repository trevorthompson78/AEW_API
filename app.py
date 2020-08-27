from flask import Flask, jsonify

AEW_Stars = [
    {"wrestler": "Adam 'Hangman' Page", "DOB":"27, July, 1991", "Height":"6'0", "Weight":"228 lbs.", "Hometown":"Aaron's Creek, Virginia", "Pofessional Debut Year":"2008","real name":"Stephen Blake Woltz", "Previous Ring Names":["Adam Page","Hangman Page"] },
    {"wrestler": "Alan Angels", "DOB":"16, February, 1998", "Height":"5'8", "Weight":"169", "Hometown":"Snellville, Georgia", "Pofessional Debut Year":"2016","real name":"Trey Tucker", "Previous Ring Names":"N/A" },
    {"wrestler": "Alex Reynolds", "DOB": "Unknown", "Height": "6'4","Weight": "196 lbs.", "Hometown":"Long Island, New York", "Pofessional Debut Year":"2011","real name":"Alex Reynolds", "Previous Ring Names":"Alex Keaton" },
    {"wrestler": "Angelico", "DOB": "7, May, 1987", "Height":"6'3", "Weight":"198 lbs.", "Hometown":"Johannesburg, South Africa", "Pofessional Debut Year":"2007","real name":"Adam Bridle", "Previous Ring Names":["Adam Angel","Adam Bridle","Adam Croft","Backpacker Joe","El Angelico"] },
    {"wrestler": "Anthony Ogogo", "DOB":"24, November, 1988", "Height":"5'11", "Weight":"165 lbs.", "Hometown":"Lowestoft, Suffolk, England", "Pofessional Debut Year":"2019","real name":"Anthony Ogogo", "Previous Ring Names":"N/A" },
    {"wrestler": "Austin Gunn", "DOB": "26, August, 1994", "Height":"5'11", "Weight":"215 lbs.", "Hometown":"Orlando, Florida", "Pofessional Debut Year":"2017","real name":"Austin Sopp", "Previous Ring Names":"N/A" },
    {"wrestler": "Billy", "DOB":"1, November, 1963", "Height":"6'3", "Weight":"260 lbs.", "Hometown":"Austin, Texas", "Pofessional Debut Year":"1985","real name":"Monty Sopp", "Previous Ring Names":["'Bad Ass' Billy Gunn", "Mr. Ass","The New Age Outlaw","Billy G","Billy Gunn","Cute Kip","Kip","Kip Gunn","Kip James","Kip Montana","Kip Sopp","Kip Winchester","The G-Man","The Outlaw","Rockabilly","The Kipper"] },
    {"wrestler": "Brian Cage", "DOB": "2, February, 1994", "Height":"6'0", "Weight":"278 lbs.", "Hometown":"Fresno, California", "Pofessional Debut Year":"2005","real name":"Brian Christopher Button", "Previous Ring Names":["Cage","John Cage","Kris Logan","Night Claw"] },
    {"wrestler": "Cash Wheeler", "DOB": "17, May, 1987", "Height":"5'10", "Weight":"223 lbs.", "Hometown":"Asheville, North Carolina", "Pofessional Debut Year":"2002","real name":"Daniel Marshall Wheeler", "Previous Ring Names":["Dash Wilder","Daniel Wheeler","Steven Walters"] },
    {"wrestler": "Christopher Daniels", "DOB": "24, December, 1971", "Height":"6'0", "Weight":"224 lbs.", "Hometown":"Kalamazoo, Michigan", "Pofessional Debut Year":"1993","real name":"Daniel Christopher Covell", "Previous Ring Names":["Conquistador Dos","Curry Man","Daniels","Suicide"] },
    {"wrestler": "Chris Jericho", "DOB": "9, November, 1970", "Height":"6'0", "Weight":"227 lbs.", "Hometown":"Winnipeg, Manitoba, Canada", "Pofessional Debut Year":"1990","real name":"Christopher Keith Irvine", "Previous Ring Names":["Lionheart","Corazon de Leon","Leon D' Oro","Lion Do","Super Liger"] },
    {"wrestler": "Chuck Taylor", "DOB": "22, April, 1986", "Height":"6'2", "Weight":"210 lbs.", "Hometown":"Murray, Kentucky", "Pofessional Debut Year":"2002","real name":"Dustin Lee Howard", "Previous Ring Names":["Benny Figg","Bugg Nevans","Chuckie T","Dustin","Howie Dewitt","Karate Durling","Mr. Azerbaijan","Rick Beanbag","Rich Mahogany","Scoot Tatum","Stewie Scrivens","Touch Phillips"]} ,
    {"wrestler": "CIMA", "DOB": "15, December, 1977", "Height":"5'9", "Weight":"187 lbs.", "Hometown":"Sakai, Osaka, Japan", "Pofessional Debut Year":"1997","real name":"Nobuhiko Oshima", "Previous Ring Names":["Shiima Nobunaga","Shiima","Fuku-bancho Cima","BxB Cima","Ape Cima","Cima Nobunaga"] },
    {"wrestler": "Cody", "DOB": "28, June, 1985", "Height":"6'2", "Weight":"220 lbs.", "Hometown":"Marietta, Georgia", "Pofessional Debut Year":"2006","real name":"Cody Garrett Runnels", "Previous Ring Names":["Cody Rhodes","Cody Runnels","Stardust"] },
    {"wrestler": "Colt Cabana", "DOB": "6, May, 1980", "Height":"6'1", "Weight":"242 lbs.", "Hometown":"Chicago, Illinois", "Pofessional Debut Year":"1999","real name":"Scott Colton", "Previous Ring Names":["Colt Nevada","Matt Classic","Scott Colton","Scotty Goldman","Twinkie the Kid"] },
    {"wrestler": "Darby Allin", "DOB": "Unknown", "Height":"5'8", "Weight":"180", "Hometown":"Seattle, Washington", "Pofessional Debut Year":"2015","real name":"Samuel Ratcsh", "Previous Ring Names":"N/A" },
    {"wrestler": "Dax Hardwood", "DOB": "30, June, 1984", "Height":"5'10", "Weight":"223", "Hometown":"Kill Devil Hills, North Carolina", "Pofessional Debut Year":"2004","real name":"David Michael Harwood", "Previous Ring Names":["Scott Dawson","Dennis Laundry","KC Anderson","KC McKnight"] },
    {"wrestler": "Dustin Rhodes", "DOB": "10, April, 1969", "Height":"6'6", "Weight":"232 lbs.", "Hometown":"Austin, Texas", "Pofessional Debut Year":"1988","real name":"Dustin Patrick Runnels", "Previous Ring Names":["Goldust","Dustin","Black Reign","Dusty Rhodes Jr.","Gold Dustin","Seven"] },
    {"wrestler": "Eddie Kingston", "DOB": "12, December, 1981", "Height":"6'1", "Weight":"265 lbs.", "Hometown":"Yonkers, New York", "Pofessional Debut Year":"2002","real name":"Edward Moore", "Previous Ring Names":["Eddie Moore","Kingston","King"] },
    {"wrestler": "Evil Uno", "DOB": "20, July, 1987", "Height":"6'0", "Weight":"246 lbs.", "Hometown":"Gatineau, Quebec, Canada", "Pofessional Debut Year":"2004","real name":"Nicolas Dansereau", "Previous Ring Names":["El Popo","Flip D Berger","Player Uno"] },
    {"wrestler": "Frankie Kazarian", "DOB": "4, August, 1977", "Height":"6'1", "Weight":"210 lbs.", "Hometown":"Anaheim, California", "Pofessional Debut Year":"1998","real name":"Frank Benedict Gerdelman", "Previous Ring Names":["Frankie","Suicide","Frankie Gerdelman","Kaz"] },
    {"wrestler": "Isiah Kassidy", "DOB": "10, July, 1977", "Height":"6'0", "Weight":"215 lbs.", "Hometown":"Brooklyn, New York", "Pofessional Debut Year":"2015","real name":"Isiah Kassidy", "Previous Ring Names":"N/A" },
    {"wrestler": "Jack Evans", "DOB": "2, April, 1982", "Height":"5'8", "Weight":"165 lbs.", "Hometown":"Parkland, Washington", "Pofessional Debut Year":"2000","real name":"Jack Edward Miller", "Previous Ring Names":["Blitzkrieg II","Jack Edwards","Jack Miller"] },
    {"wrestler": "Jake Hager", "DOB": "3, December, 1982", "Height":"6'7", "Weight":"275 lbs.", "Hometown":"Perry, Oklahoma", "Pofessional Debut Year":"2006","real name":"Donald Jacob Hager Jr.", "Previous Ring Names":["Jack Swagger","Jake Strong"] },
    {"wrestler": "Joey Janela", "DOB": "4, July, 1989", "Height":"5'8", "Weight":"183 lbs.", "Hometown":"Asbury Park, New Jersey", "Pofessional Debut Year":"2006","real name":"Joseph Janela", "Previous Ring Names":"N/A" },
    {"wrestler": "John Silver", "DOB": "4, June, 1990", "Height":"5'4", "Weight":"149 lbs.", "Hometown":"Long Island, New York", "Pofessional Debut Year":"2007","real name":"John Anthony Silver", "Previous Ring Names":["Johnny Silver","Rob Grymes"] },
    {"wrestler": "Jon Moxley", "DOB": "7, December, 1985", "Height":"6'4", "Weight":"235", "Hometown":"Cincinnati, Ohio", "Pofessional Debut Year":"2004","real name":"Jonathan David Good", "Previous Ring Names":"Dean Ambrose" },
    {"wrestler": "Jungle Boy", "DOB": "15, July, 1997", "Height":"5'10", "Weight":"150 lbs.", "Hometown":"Los Angelos, California", "Pofessional Debut Year":"2015","real name":"Jack Perry", "Previous Ring Names":["Jack Perry","Nate Coy"] },
    {"wrestler": "Kenny Omega", "DOB": "16, October, 1983", "Height":"6'0", "Weight":"203 lbs.", "Hometown":"Winnipeg, Manitoba, Canada", "Pofessional Debut Year":"2000","real name":"Tyson Smith", "Previous Ring Names":"Scott Carpenter"},
    {"wrestler": "Kip Sabian", "DOB": "19, May, 1992", "Height":"5'11", "Weight":"183 lbs.", "Hometown":"Gorleston, Norfolk, England", "Pofessional Debut Year":"2010","real name":"Simon James Kippen", "Previous Ring Names":"N/A" },
    {"wrestler": "Lance Archer", "DOB": "28, February, 1977", "Height":"6'8", "Weight":"276 lbs.", "Hometown":"Austin, Texas", "Pofessional Debut Year":"2000","real name":"Lance Hoyt", "Previous Ring Names":["Breakdown","Dallas","Hoyt","Lance Hoyt","Lance Rock","Lance Steel","Shadow","Vance Archer"] },
    {"wrestler": "Luchasaurus", "DOB": "10, March, 1985", "Height":"6'5", "Weight":"275 lbs.", "Hometown":"Los Angelos, California", "Pofessional Debut Year":"2009","real name":"Austin Matelson", "Previous Ring Names":["Austin Draven","Austin Morrison","Judas Draven","Judas Devlin","Just Judas","Vibora"] },
    {"wrestler": "Luther", "DOB": "30, October, 1968", "Height":"6'1", "Weight":"251 lbs.", "Hometown":"Calgar, Alberta, Canada", "Pofessional Debut Year":"1988","real name":"Len Olsen", "Previous Ring Names":["Atomic Punk","Dr. Luther","Lenny St. Clair","Lenny LaFond","The Masked Canadian"] },
    {"wrestler": "Matt Hardy", "DOB": "23, September, 1974", "Height":"6'2", "Weight":"236 lbs.", "Hometown":"Cameron, North Carolina", "Pofessional Debut Year":"1992","real name":"Matthew Moore Hardy", "Previous Ring Names":["Broken Matt","Damascus","High Voltage","Ingus Jynx","Ishan Hardy","Matt Hardy Version 1.0","Rahway Reaper","Surge","Wolverine"] },
    {"wrestler": "MJF", "DOB": "15, March, 1996", "Height":"5'11", "Weight":"216 lbs.", "Hometown":"Plainview, Long Island, New York", "Pofessional Debut Year":"2015","real name":"Maxwell T. Friedman", "Previous Ring Names":["Maxwell Jacob Feinstein","Pete Lightning","Sandy Bunker"] },
    {"wrestler": "Marko Stunt", "DOB": "30, July, 1997", "Height":"5'2", "Weight":"unknown", "Hometown":"Olive Branch, Mississippi", "Pofessional Debut Year":"2014","real name":"Noah Nelms", "Previous Ring Names":"N/A"},
    {"wrestler": "Mark Quen", "DOB": "12, April, 1994", "Height":"5'10", "Weight":"210 lbs.", "Hometown":"New York, New York", "Pofessional Debut Year":"2012","real name":"DaQentin Redden", "Previous Ring Names":"N/A"},
    {"wrestler": "Matt Cardona", "DOB":"14, May, 1985", "Height":"6'2", "Weight":"224 lbs.", "Hometown":"Long Island, New York", "Pofessional Debut Year":"2004","real name":"Matthew Brett Cardona", "Previous Ring Names":["Zack Ryder","Brett Majors"] },
    {"wrestler": "Matt Jackson", "DOB": "13, March, 1985", "Height":"5'10", "Weight":"172 lbs.", "Hometown":"Rancho Cucamonga, California", "Pofessional Debut Year":"2004","real name":"Matt Massie", "Previous Ring Names":["Max Buck","Gallinero I", "Mr. Instant Replay"] },
    {"wrestler": "Michael Nakazawa", "DOB": "8, October, 1975", "Height":"5'11", "Weight":"203 lbs.", "Hometown":"Kawasaki, Kanagawa, Japan", "Pofessional Debut Year":"2005","real name":"Masatsugu Nakazawa", "Previous Ring Names":["Abnormal","Nakazawa Magic Iker","CEO"] },
    {"wrestler": "Mr. Brodie Lee", "DOB": "16, December, 1979", "Height":"6'5", "Weight":"275 lbs.", "Hometown":"Rochester, New York", "Pofessional Debut Year":"2003","real name":"Jonathan Huber", "Previous Ring Names":["Luke Harper","Harper","Brodie Lee","Huberboy #2","Jon Huber"] },
    {"wrestler": "Nick Jackson", "DOB": "27, July, 1989", "Height":"5'11", "Weight":"178 lbs.", "Hometown":"Rancho Cucamonga, California", "Pofessional Debut Year":"2004","real name":"Nichlas Lee Massie", "Previous Ring Names":["Slick Nick","Jeremy","Jeremy Buck","Gallinero II"] },
    {"wrestler": "Orange Cassidy", "DOB": "4, May, 1984", "Height":"5'10", "Weight":"161 lbs.", "Hometown":"Stewartsville, New Jersey", "Pofessional Debut Year":"2004","real name":"James Cipperly", "Previous Ring Names":["Fire Ant","JC Ryder"] },
    {"wrestler": "Ortiz", "DOB": "27, September, 1991", "Height":"5'8", "Weight":"192 lbs.", "Hometown":"Brooklyn, New York", "Pofessional Debut Year":"2008","real name":"Angel Ortiz", "Previous Ring Names":"N/A" },
    {"wrestler": "Pac", "DOB": "21, August, 1986", "Height":"5'8", "Weight":"194 lbs.", "Hometown":"Newcastle upon Tyne, England", "Pofessional Debut Year":"2004","real name":"Benjamin Satterly", "Previous Ring Names":["Neville","Adrian Neville","Benjamin Satterley","Jungle Pac"] },
    {"wrestler": "Pentagon Jr.", "DOB": "26, February, 1985", "Height":"5'11", "Weight":"207 lbs.", "Hometown":"Tijuana, Baja California, Mexico", "Pofessional Debut Year":"2007","real name":"Unknown", "Previous Ring Names":["Dark Dragon","Pentagon Dark","Pentagon geci","Penta El Zero M","Penta El Zero","Zaius"] },
    {"wrestler": "Peter Avalon", "DOB": "14, June, 1989", "Height":"5'10", "Weight":"169 lbs.", "Hometown":"Carson City, Nevada", "Pofessional Debut Year":"2008","real name":"Peter Hernandez", "Previous Ring Names":["Norv Fernum","Adam Jones"] },
    {"wrestler": "Pres10 Vance", "DOB": "15, January, 1992", "Height":"6'2", "Weight":"240 lbs.", "Hometown":"Clare, Michigan", "Pofessional Debut Year":"2015","real name":"Cody Vance", "Previous Ring Names":["Cody Vance","Cody Vincent","10"] },
    {"wrestler": "QT Marshall", "DOB": "15, July, 1985", "Height":"6'0", "Weight":"234 lbs.", "Hometown":"Livingston, New Jersey", "Pofessional Debut Year":"2004","real name":"Michael Cuellari", "Previous Ring Names":["Michael Q. Laurie","Mike Marshall"] },
    {"wrestler": "Rey Fenix", "DOB":"30, December, 1990", "Height":"5'9", "Weight":"185 lbs.", "Hometown":"Mexico City, Mexico", "Pofessional Debut Year":"2005","real name":"Unkown", "Previous Ring Names":["Fenix El Rey","The King","King Phoenix","Mascara Oriental"] },
    {"wrestler": "Ricky Starks", "DOB": "Unknown", "Height":"6'0", "Weight":"195 lbs.", "Hometown":"New Orleans, Louisiana", "Pofessional Debut Year":"2011","real name":"Ricky Starks", "Previous Ring Names":"N/A" },
    {"wrestler": "Sammy Guevara", "DOB": "23, July, 1993", "Height":"5'10", "Weight":"145 lbs.", "Hometown":"Houston, Texas", "Pofessional Debut Year":"2013","real name":"Sammy Guevara", "Previous Ring Names":"N/A" },
    {"wrestler": "Santana", "DOB": "4, February, 1991", "Height":"5'10", "Weight":"197 lbs.", "Hometown":"Brooklyn, New York", "Pofessional Debut Year":"2007","real name":"Mark Sanchez", "Previous Ring Names":"Mike Draztik"},
    {"wrestler": "Scorpio Sky", "DOB": "1, April, 1983", "Height":"5'10", "Weight":"205 lbs.", "Hometown":"Big Bear, California", "Pofessional Debut Year":"2002","real name":"Schuyler Andrews", "Previous Ring Names":["Gallinero Tres","Harold","Mason Andrews"] },
    {"wrestler": "Shawn Spears", "DOB": "19, February, 1981", "Height":"6'3", "Weight":"223 lbs.", "Hometown":"St. Catherines, Ontario, Canada", "Pofessional Debut Year":"2001","real name":"Ronnie William Arneill", "Previous Ring Names":["Tye Dillinger","Gavin Spears"] },
    {"wrestler": "Sonny Kiss", "DOB": "11, December, 1999", "Height":"5'8", "Weight":"187 lbs.", "Hometown":"Jersey City, New Jersey", "Pofessional Debut Year":"2013","real name":"Hassan Aziz", "Previous Ring Names":["Exolicious","X O Lishus"] },
    {"wrestler": "Stu Grayson", "DOB": "25, January, 1989", "Height":"5'10", "Weight":"193 lbs.", "Hometown":"Victoriaville, Quebec, Canada", "Pofessional Debut Year":"2005","real name":"Marc Dionne", "Previous Ring Names":["Generico Dos","Player Dos","Stu Dos", "Stupified","Zombiefied"] },
    {"wrestler": "The Blade", "DOB": "3, June, 1980", "Height":"6'0", "Weight":"220 lbs.", "Hometown":"Buffalo, New York", "Pofessional Debut Year":"2000","real name":"Jesse Guilmette", "Previous Ring Names":["Pepper Parks","Braxton Sutter"] },
    {"wrestler": "The Butcher", "DOB": "Unknown", "Height":"6'3", "Weight":"273 lbs.", "Hometown":"Buffalo, New York", "Pofessional Debut Year":"2016","real name":"Andy Williams", "Previous Ring Names":"N/A" },
    {"wrestler": "Trent?", "DOB": "30, March, 1987", "Height":"6'2", "Weight":"215 lbs.", "Hometown":"Long Island, New York", "Pofessional Debut Year":"2004","real name":"Gregory Marasciulo", "Previous Ring Names":["Ace Vedder","Barreta","Greg Cardona","Greg Jackson","plaZma","Trent","Trent Barreta"] },
    {"wrestler": "Wardlow", "DOB":"19, January, 1988", "Height":"6'2", "Weight":"267", "Hometown":"Cleveland, Ohio", "Pofessional Debut Year":"2014","real name":"Michael Wardlow", "Previous Ring Names":"N/A" }
    # {"wrestler": "", "DOB":"", "Height":"", "Weight":"", "Hometown":"", "Pofessional Debut Year":"","real name":"", "Previous Ring Names":["",""] },
    # {"wrestler": "", "DOB":"", "Height":"", "Weight":"", "Hometown":"", "Pofessional Debut Year":"","real name":"", "Previous Ring Names":["",""] },
    # {"wrestler": "", "DOB":"", "Height":"", "Weight":"", "Hometown":"", "Pofessional Debut Year":"","real name":"", "Previous Ring Names":["",""] },
    
    # {"wrestler": "", "DOB":"", "Height":"", "Weight":"", "Hometown":"", "Pofessional Debut Year":"","real name":"", "Previous Ring Names":["",""] }
]


app = Flask(__name__)


@app.route("/api/v1.0/AEW")
def AEW():
    return jsonify(AEW_Stars)

@app.route("/")
def welcome():
    return(f"Welcome to the AEW API<br>"
           f"These are the available endpoints:<br>"
           f"/api/v1.0/AEW <br>"
           f"/api/v1.0/AEW/wrestler/Chris%Jericho")

@app.route("/api/v1.0/AEW/wrestler/<wrestler>")
def wrestler_by_name(wrestler):

    canonicalized = wrestler.replace(" ", "").lower()
    for wrestler in AEW_Stars:
        search_term = wrestler["wrestler"].replace(" ","" ).lower()

        if search_term == canonicalized:
            return jsonify(wrestler)

    return jsonify({"error": f"Wrestler not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)