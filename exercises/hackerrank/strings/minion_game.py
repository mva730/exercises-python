#
# I had some trouble with run time errors initially, I was making it way more complex than it had to be. I find it helpful to note that the number of subsets starting with a letter is: the length of the string - the index of the letter. I.e. if the string is 'banana', the number of subsets starting with 'b' is len('banana')-index('b') = 6-0 = 6 : [b, ba, ban, bana, banan, banana]
#
# Using this method you can add the number of subsets starting with each vowel, and the same with each non-vowel.
#
# for i in range(len(string)):
#     if string[i] in v:
#         c1 = c1 + len(string) - i
#     else:
#         c2 = c2 + len(string) - i
# You could also make two seperate lists - one with the indicies of each vowel, and one with the indicies of each non-vowel. Then get the scores by calculating the length of the string * length of the list of indicies - sum of the list of indicies.
#
# for i in range(len(string)):
#     if string[i] in v:
#         a.append(i)
#     else:
#         b.append(i)
# c1 = len(string)*len(a) - sum(a)
# c2 = len(string)*len(b) - sum(b)


def minion_game(string):
    vowels = "AEIOU"

    stuart = 0
    kevin = 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


def minion_game2(string):
    vowels = "AEIOU"

    stuart = 0
    kevin = 0
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j][0] in vowels:
                stuart += 1
            else:
                kevin += 1

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


def minion_game3(string):
    vowels = "AEIOU"

    # vowels_num = 0
    # consonants_num = 0
    # for i in string:
    #     if i in vowels:
    #         vowels_num += 1
    #     else:
    #         consonants_num += 1

    stuart = 0
    kevin = 0
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i] in vowels:
                stuart += 1
            else:
                kevin += 1

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


minion_game2(
    "BYJKTGJFIFVMRPFNFKATRQFORMGKTQCLZTNBWNSORUVBPKGJVSRMQAATCYZGGTTOJOZNXDYWKEJWUAHJKDJWBAPOYUVFKEMYWNBJXCCYIYLLLTAUNJTPMJJEPWOPNXLRQUKHDMEUKWUMSBLTFFYHMCGYYMHOMJDTNAVYDINWSDWBSNGIURHILNWRXSEAIKEFAUEFNHQIRESGQSSAGBOWCGUVWHKJXHUDIXVXRHOUKHUXUNDCSNRZYFDEAUYBWHNKVBLMRZZBDMDZEXPSLRUFFKMPHVQDDPDOYTKLHIVMKJVKGFCEKXCJQZXOZYAWRABDNYKUQYTXNRRVWWSLFOZCAOVZVMYMDTJTFJQCLJAUUADSBCPHMPVTIPWNQNUPOZPNATMJAQXEKCBACJNWETOTBZRHOBBGGQFWOKCMJYMZSHJCACSLSINKJJMUOERKUHBDISFXJTZDMJLFVZJIPBVACVEZTJXHIQPALEYYOVXGHQENCWCQPSDSTRQBGCYNCWANBEJIDBXFJVONTTPIIYYSVLNEHELAEIXYNWRVNYRWYYZABAKEPPBGECOHAJAJZKMKLSDJCEEOJFRYCUEARWPJGMISBAETOHUITGGFSXSDHZMAGIEUNQEZWVOTCFMSCHTYVABKONCBWQLVYCEDEEAGMORVYEIXSHEXAIDVFDTSLFSHSMHPQNWOQBNNIBNEXPNYPXHUFDERDNVPNRCFJCZTDKUOZOSTPCFIPMXCUVXHENXFKRVUVCJKLLEGXRXWRVJLCXHSSNKIMRDIYMOIKHHXGWZXRSCXPBVODPDVQRLKTZITKDDADTLVYCAYZIFOYRMMBIVWOZJXKYHRVHUWKIZWALJINMWUXHALRGPTLHZIDUAFSTNZEABAUMWGQBNXXBMNRBQROERUDHUFXCLKCQKNYTBWDTLAAPRWCCVQKDHXBCYSTUGVCEQEEZRZETWJDBFPIFSQNCICXEDWCIQTZUENUTHVNZVTBIZUROSAMTBWGCTYGNEJIVQIKPPTVXTXUBDKCGDYIQTPVWGIFBMFEUWRUOFWVNFEDDXAPFXCULGZXSBIPPGMFXTLORMJQJIRFFLNQJLLEOQXDFXWOXKOYTBYFTHEWLFMLFCPKJCBIXDEXGJSACSLNWYVDGMOFPHLTQRDEMJWSPXQTNNOOIVRXQLITSCATSAGNRXJFQHEORNSGMKKDDCAZKWLLZURYNVNVRSQJFVEAWKVTBMYDBSNRFDDGPDEUOJHMQLZYBYCOJDQYFVYCTERCUBJYEDCDWFNRLPVZRTZOFHGXOCDRQWEIJTEQYHJJKUCODSMLOXRVZNJPMTYDUZLQHWVPLGERREIRYFCOWXLJRDXLHFTZFAWUACTGDQNCQJPGTEBIGUFBZTKXHYJCVOEHCYRJVLMPVTMGPNWJHXVFZGRNJBFECVQTAFSCRILSKLQXAVWFZDAXGVRQXPBNLKUZORTXLIEDVNXVBYPRDZBKYHAYCWZDIDBGPSYWHQNPOLKPNBBEJQISDLHGXTZYTDQCCMMNRSCLBUXZVSDGXROLFUFVRXLSJRPIJIIJCTSKYADAVWKKGGPCWYBXAQRCGRQHGEAEFOCYEKXFJJKFEHTZVSSMUSRCOSXJVJUYHXKEZVUJDXITFOISVFZQZOOXBPEHZYHBTBCGVVQYBSAHRNSDCTOXMETEXCFZOWPRHFYDVPFXBVVKIZTSYAVRDYHQYXDHLERGHOQSTYHOUGIMGPRPSKDKOFSGGZUCKHWUAEBIRCVDQFERTXGEWRKFEMBFVXFGKUUMYEMDWIIZNMTMQQVHRVMSDBGWJFUWNTXSZXGSOIVRYHKETMKTCEHKVRWRTRNILZSKIJARXKLYYTOUURWGXOAIADQSAIMCGHWPYPTPCQQBOUYBZJONXINCCDLKGSUDRZHRHZGJUGWOACMXFMWAMUWJQMCSDCZLGMQUFWCUFOUSYPOEFEFUGGWDMFVPVPOMCANKRZTLENNKAQCVLPPMYHUDYSXHBHGWGVNPQVHZEYNVICBPCXULJMUZQWXMISMQQLEJUEVISOSYKMCKOHCIPVBKMSVAECGMTPPSSKZJFVBEZJRHXLFGYAERYCYZLBVWILFQYCPCCBBNMULRSJHEHSUGXBYUHIOJEBKWUSSYKYZJXYMMWKHAMPRTOZHFEYRMZMJCCEIBCYMKFDSRWVQVKDILCGKDANXIGMLZUEXQMNWNPAWWAVIDMBIDQRRNTODNMUCGDHEOSJYFOSUNIHKLOOXRWFIMLDPNELGDRGEYUGAOCBLIDZSWDCYBNVLEQLYAKXQZIKFROPEWZQAFFVKROCOGZJGOSIWAMDBIRENZOXEIMLWJZPFYWFISVEBPLGSUGYLEJIZBCCSLDDHFLICGXUOTYRHHNOFMQSFLJAGVGGEZFODFYCCRRHCTQGPLRKGKXRABFYQAIIXUIHBTMRKCRKINDCQEGEQTLQUYZMSTVSCHIAZGTQRVOBVCNJNVGDCMWYMNEBQTCBUUHUNYPMTONLXVTGPSMJVPHJAFOMDUSOFSXGNCPESLKSNRQBEBVBGUHNDCCNIFCPRZCLSUVAWPNCWJBPLBRMNJKSOVEUXXTRUEPZCLJGUETFKRYSZELKHBYIOGFARYLQEHXKQBLDSUBWWGIDHDOHQWDFOJPXDEFTRMEHSSHJBQSAJXQNTZLDMMEFTGABFDJFOAWUCPNTEMEEKCLCBVAXLRNRHXQISTWKEBXPFNVTBTLQOMUBYCDSIHPEYCSVHIAYPUDWCCAJNBJHZPXAEVRELJUVGLHGPHVBIGXSRNECIIANHAKCBYKWWXBOYVCGYZGGULTQBGVUSXXGUMAYKIDTZSLVJMZINNKZAKVXUVHOGTEHQJZVSNGQPGFQWJIZKUVDVSNHXKGRNTAKFPYRLEZEAWDAUGDHFNOEDQUQCGTJJBMOMPGEXWUURXMKNDAYSCPYOJUZQKNVXYBUXGGGKEJCTQYGMJZCWKSRHCWQRLEPOGERNFDYYZEVSGJJOXBDBKTMQJCSMUHMEKDBNFRTTOEZHWAYTQRMZPGCDPMCRPWCGUBQQTPOZOTAINNHQNTSIKJBERNOZZKQFJORWOAVWMHKHBMBXDWGMVYGQAFVEPKINHYWQJYBMBYWILSVGQSBQZLIHNHKNVIOOIWXZIDBBOWGGTJIBOZYDMOFYLLCXKVUOYTAGRFOKMYRYODATNPRLTCXZGOAVVBLCLYQDRLECGBZQHBKKZHYKNHASCEGUYKAAKDYQERLTWAWCZZPUNKILCEVPLQLWOZJIXSSBUIZFLOMKLRBNWXKTUYWIJLAGUFWBHTAUZVMUNQLGZBAZAOQCAWPTYKRWDDCFQQKSYVSNJLIUMRTHHRTELKTDPUUOZTHNQZRVWHARNGKGJHPHFBALKTQNORHJWNDKIDHDONVLHQKUYUZMZWMBLPTQQDUQFGJMWZDGTKCWDMHXYEMVSRMNXVUTWDCKTZQPSCQFQBXTJOYHZQPHEYRBUDKCPMBELTWSYOQKOQEIJKDSRWIIOXDDVJNMWNQJSUXXEJXDGWDWDPEMQHLHLFKXODZWXTSWSJUYEQDPNCIPYRAMRRSPIPLTJTYUSHCSRMYUMIIUUXLLWTSEKQNCLYAERTTRDSMSOBCALBQVMRCCSQQKHFEQNSQIKOZHGXIVOUIGNHFDUWGACXSQEEMQHTJJHWWMOMPWLAXNCOEFDHJPMXBMHFZHUSFJOUHUHLCCAILHCJFGCBWIGDXVBORSEKKKNRHFGCLBKTRKZMNKLPCURYKHAPZLTZRXEVJODRDCQGWIMYOXEWZJCLXJAXUGCWTZVPUZJYXDVVWAWQZFXLTWJNMSRICCDFDLWEZIDUBIPCZZSIYOHXEQOSLUHSCZOTHMBLYDUZLUICAVKSWQJIPAARWXAWJMPJPUYCZDPHXLZQVOACPHRQUGWTZYDCGSUIMHOPLQWDAWUATOPMLFFYGGXADZFQKGNCQYUFVOCEOOUSBKVXDPXAWWGPGVVFJVTQHLUUNHAGZUPFUNAMTZNDHVNUANSOZLVXJFJQVTRATDFWBTXNKZWWQBATBEAUEFJVNWYWHQVDXVZGOHODBNORWFOCZPWUDBIDHLNHKNEIRTMQEKOSRPCDELEMYPRLWOTAXEPCGVCEKWEVCTEVZZHSMLWOMSWSABINVIFAOSGMXUSGIZZNANGALWAFWYEBLUGERMHDTSSQGYHDSUCYCFELQSOVEQBWPBTAHYRHIXJJIEBSHLHIKTWYRYRNFUPGDNPPULVGKAFCMTXZKRFWNYEAFBFZCHERJAFHGOHHDWUGVPTUBJUBWXNQJFWETPJDKGKKEJGXYVFLCSNQSEYBZKDNRWFEHWOBVUSCVFBQHWSXYCNHEINOJDVPNZTDOJGMFJYHJNJBSCDJHMABWPSCTNQHXRXUOKJGTWJGAYPVWUBDADHWQIHMNTLHVSHTCLCNFLBPCZTGEGKDQITJLWABOWBMGUJBWFRRNYYEHWTLLOXYTACZXSTLMJYEMCIDTNWCISIELSTKKLZKTCNRXKVETECAOZKXBPODFAJCHOADCWJSBWOSWOFTQHTYGBQHBBKZNLWTVOCXCCUKIFTTCUFTNNPAUNHNOFZMRHUFGNFKAUGLQACOCYUWBZPIDYMUKKNXPCURJSSBBDCJKCAKGCVUKUMCKEPLTOVPENEGRIJLKFUBWZETGYFSIAAAYBLOCUTZUIPAJUNKEZFPMKWNOXZDJMYCNOOYDSKINAFBKTANBOCNZFAPNJRLWXNCZHJSLQZOKGVDPZELYJNWVEHHSDUZIZKYVWJJSYLJVRUEWAIFTIEQHLGDLVVMYRMPFEDNSVIEELVLBKRPYLALRGYFNIDZBAFQPZJIAWDXEOKBNUGVDGWILVHCWEFNOVPFSLBZVEMFBTFAFOHBQYODZZWRPXCGNLVQHEHSRBGFVEKWCWYGAKZJNCTUMMDVGJYXXURHZOUFDEHOKFSGLKOAVNCDBVIHMVGPXTINKULXVPQNOFQWZSYYILMPMISSQTQWJHAJXFLZGODGEGZMNCHIANTXODXLMIEDGCWMBDVODTAWYCRIAMHXLFEHJAAVEOHOFWTSLIAYZBXLZFPGKXPADROQSTEPBRODVYUMNNRGSGQWVEKOUJGKVNGJMPOHTCJOXPQUQKYYEAZYXAHNOHCYYSIBCHZMGMXEPDXZNNZGXYMCCFBXJDJBMELFSVMFGXBEKEQJNPXYYPRRTNGVRSYIKNQSNAPGXETNUQMHKUSGMLATOOEXKDTAPOFCRPMOWKKKJVLEIRAIRTZVRBUUYUGAECXXIBISXGTVIQYPFEQYHYWPNRVBHGPQLFXYPHXSVUVBYCXODXLSWKGUGIPJZHCGNLHSAMISXBFMJNAUBBFHQNNTVPWUVHAGGQSQISZEMTGIKOHWDLRFEZWGXGBUOTNTPJSSUKZTYRUUCXWNBLLABWFKJDBZQQSCRTORNLOMUNKMNDJWCQXRUPUMGWXPQKKCVOGFNFTCQYFIAVXEKTNNZKHWSKVVRRYWXUHHEJONPYMVHEJERMSNESSBBMVMLFDSOLDJOCNGBPSYXZSKJPFZOABBPNVVRZALISKTFNTVMRFBCXSVUACTYKPDKQVZCMDEVWRRGZRLQKBFCFVEOZXFTDTCXTJZXRNPSYSYIYJQYJUYHOMIPBIHTYKIEOOATLXXFGZDCBTRNVWTFIYVWRTPUEDIRLOZKZOMVYECIZNPRCTJJBIRCIIFDYCRXGRFPHKERXXREBZPQFHBVHEWFHUXCRZYAYHAAJGDKHNBZFTMRONTTURPRJCGTXRQYUBYPACSDCXIRGISPFVKLEKMZKMMODNXEAUUOYIONJYBQYTQEOSRDFRACUQNQLZSNMNBXMOTBUGOSEQOYUFWONAYSPZQSFTOTJUSNWAERHRRGQWXYVBRHJQKTLHXQMRTBDPRXSOFUMUECMPAECOVNJIQJNOIWBTJIIHXGJDFJFOPIFOTQLDTIYOEYLSHBFGHHIGEHNJFRVYHOJCFGELHQBFVMOVXSFDAZYRHELXGPXFZDOWATTQODPFABKAOQWIBRBGFXLCDQDBJWBHJFSCPRSMDXIHZENNSAPOTPQVGNPPYORXGCJZHNORSFYZOPAVRJSKQNTVSSJCEKUOZLBIRAANSIEAJDLXHMRXTDMYKINNKKDGDBXSRFFLYTYXBABXTBKZQHWWYSWDQTNIIRHMQYGBNMMBZGVUKQZEMBTUFUOLMBOPNIDDSFVQGECGCFJNMQKAYRPLMLLSUZZGFAYPEDEFUYAYBZEDADMQUYCOGDLDTFMIJDQCYCFPPHKWGNZEPCLCGDLOLBUNRZSBVWLBHLIQAYVPIKHMLOPTPOQRGBZOSERRTUMYQDWCNDHQMSONVTRZRBXOGIRRVZPEOZBRAFNACIDKDHUXOPZCBAXOWOOLTPOKXYASLQZHBHVGHMUOUOEOLSZILYYDWOZAXJULFIFFAJUCTLEUQLBVTWPKODKOIQMNFPSKFNWKWAYLNGRITZEKQBXIJRBGWBCJYISISXRNNLHDNVSWMQWZORTZOJICNZZOTZIZRCUMJHXLSYPWUAQKWYOQDVQPFWFYFHMGUOFEKIEZQLYSVLNJMMGDNKEQIJLXMOOMSXHMAEPUGQYJITLIFYOORQARWXLJNBSFXIPWOOKBSTFVSBZZQEQESUIVWCUILKEDARJSADCUFPCIKUORSPHHLPTBTOMSGIFYFONPOQLQNLVHWQFKIDHEUWQJZTTYLMVAJWTAZCJMHWKNFCQJIUSCOWUEPTPETSFOSFEHBGGTPXCAPBPPGUVCEKZSAGAGZKWJPFEQHYTUCTUVZUTMPHAVZAFCKMJZXIPPTDMOIFIBPDLWVMKVEYKQMFQKXPWJQXKQOAOBPFBOXPOETPHQSIXPPXTHWKXRBTWJZARSWFJKGASWSRBPDRCMRDPCROGGVWLDISWUQVHZYNPFQFKDAWNJJLBSDTTJYUQLPULRHIPXVECDBEBZLXHTJFMYOMCFQUWKMQIYKSRJTCRQIEIOVCQJNFOYTHOKNVGVFSDTPACIEUCKWOXRKFIKGNOXFTPDMASLTYGLSWZBUSBQMNWBGQTVXFYBSAYHXFKTALNDTINAUSBGVZHNYADBJFTXAPSXJJPASGBXEGJDZSUKLBRDPDJUSBGQGAWVRGNXNURJUTDPDOUKNLLNLGHGPFLKWRZFDYPVSUGNJHEWIVGJAMUBWPZCYZVMAIONMZMDOXWGYPCDOLMNOOPSAJXORMHCFKYAZKMGBZFGXDIVJMQJLLXHLKIYIOHZJRFDRCLQBLNPFMJWAFBFLGXRAXISKLHYBPRLAUCBSAOUXTFEGCAPKUCEJWOJQJERSGUVNPHDPSASWABUWTLIRWBZLEDCSIMFDSTIXFXREZOIMPQFZOXZJKUQJNKSTURHHGQXVKAZLGAJHGYHWLBHUFNLYTEOLAINWBRCHETQEIULMTHVTHBBGPHWAUGDERKKMGMRYZDFPPCSRDCAMVERJCQLWFFFTFRVJYUNKGHROCLKCPVJNEHAYDYVDCWHLCJWHEPSOEYFCNDGEAGGRPIWEFWAVAITOCDYDKKQPTANDOUEUTNUJHWKTHWAGLNWULFXEICGYNAQKTKKNPRHFEXDZYIBDEIGCSMSRGCXFUIQXICWJRZHJZUINXGYSQQTLBIOBKOAQMVBOKJNRPTAWFXCCIXRQYBUMDPHOZYNTZZMXCHMQJODBTHWQRSPTHPUGXCVBXFVTUGKFRVHOIEQYAHDGEZTEUERWPQFRHBKIXMTJXCRODJAICMABPFOBSGNCSTQJBPWGDWBVNOJGAMOAANSOXRJGAFFUIGETMGLVHFSHRYSSUYVAFEKLLLSBKPHDCJCPQNDPDGWFWNZXQSIRVEYKXOUSWQXAPEEORSYTQVQLCMVDKZHAPOAHSFTSPSKXHOCHWHGDYHEOSCPAKJKSMFMZWUAKKHRYKJGDRZNWDJYTFHVTTOWXMYSBEUYTDSJGRMRMAJZVKFXJTIGPZHXQFISQHGJYQSRZNSKKHHVJHOPIILIUUZDBXKPYZILNQFGWWUIFDUGUQCKRFZNEOXMTZOHWSLKPGXSMRNTZVWRWQAEXTWNAWDJMQOHXZRAOXIDPCLDJETJLJCPPCEBMEIFWYTNKILNOTVVNTQEDPAROFXMUFKKYNHXJYPFTJTVWTILPUHRGXWWCNVMRHKLKGGGRJUKRNNFOFMLDUZVRKVJMVJRMJLPQMOZYCGCUNWAAXSRKLGQXICJOAYKJOWXCOLXTRQNRRQGVOXUWCHYSAQMLPMREIRNOHPTRCXCBEYYGRMLYPRJBLLFFNCDWVKEBBUYHJLGLLKEGGCCLBBPPKGMPMGORKNASRZWQWABXZJIIZVPJUISIANEINBWPTJKPVQNTXSMFLFHRYYUWHYWPTRFWZASYQHTHLMTFVMETHLAFYYMZYAQTWLPYTDAJXOVRQGSPFDXDJWAFPAYNNEESPKWTPWHSVJKINXCCXGLXPJFDZPNDMJZOCFJHEKISNVOJFIPSCHCGAFVVDXCVKZRIFNAGLPBLIBGSBVMUJDWXEZSXOUNFWUFPQZQPYFSPRFRBDQAIIXATTJADDWNHARYVWMBCTIRIGMHZPMQROHWDEOAYTBTWALXPKRPWBSLFROWRMGBWRCCGHMMTMODRBQNXEFBFWHTAWMQTRNFSDIKRKKHOZKFNXPAGFBWUVUTXYMSRHSJLCUUTVXWRVNMXZXOFIRZIMXAXUWTWMURTXVHODPGCVADBXUUCHSGSYSBDSHJUPDGSNPYYDJVMTYCVFNVUBQFBBVQNXTHHAFJJJHAMOSPDOEVACHYBRUIAYKXWRXRPZQCUVOTTUCHJXWVGWQWKVYBWJWWZEZCFMKZAUBFJXACQCMEJOGZWYTPCQKXUQXZMDRVDKBJSMJUCMSWGECVROXIHOAKZUBTEWMTLPOJKITEIILUXIESCHNLDFFLKONYKGJPSCHNYCCMWPWBLMLVEXNKNRSEMYDBXDAYCOFIGCHTUFXTMWJLYYRYYKUYDBGOESBUMBCXVDDRIEYAAAWJDEOXZNHCQSNPANZNBAZUNLLRXJIKBLZKGBVGRZHWQLXFPWLIFCCXOOPBARVBYEJIDSYRKUQXVJIQFGFBVATNIIFTPQAHZPPHCMBAPJGBEVPXEZNOUBIJEKFWAEHEEKTUVHOJNPJVMDWPXXINTLDCDYDNHWIODLQEMPKSFITFUOTWCLOUNJKSCSHZDOABHNPXEQPGDNSAKZMBKVCPSJCEVLUDOMILIYUDRACDBIFKAXEXUQHXZATWOVXTNJNBTFFPAQRPJHIMZWYERERURXTUXWYGQOLJZGIESXJAKXXQXECUYZOWUSVLPGSXHETRPTFVFUERPACNWNESZMPTNHMDXTIVTSUNHEQYYJGPIGJZHNVHWXCPVKZYWKZZVUVKFCUWHVCGDNBUYOWAUPCQOKLRFPJJMFRAIAVZOWBJZNZIWJGPBCTKARNPELTZOQYBPWTOUIFYJXCKVJAPRASCWXLQOHNWGQOXXGSXAITISVAUZPFLVAXRFNRESCKPDIDTQNJGDHQDJMOXBVJELUQIUQVRSUYAZRTFBXNJXADHSMRJVDRJAYMGNRTUTWWZXJEMRBVYMMDVNDXDHHJDQQLDVHAYCAZNFFATVSKDKGMVZXEJZLYHPLYOYYJUTVOMZGXPZTFFUFZIWDPSWNSEEDZGGEDKPUHZORYNGWBZIKXJLZEUMZNKMPJWTZKGQOUXCDMEQFLPINZZMAVRRIIOLDRKEGXJNMVIVIRNILHYFIYOCGFRDDXUGUWIIDYBIVYSHBQOSJMBOUFJFEBMGJJSUWZZPUSRAOWFRGFXKVTYXQOTKAMKPQXUSWOHWDWETBXOZXVWXBBAXQDYVMYUSROHYFTQBJMSUAWXOUXKSEWFMDXQCKGSXEZDSMGZFEHHZJBMJSZPDZKVVCCRXFRVHOLWCSDAFVXRXFAZOJSZXUXLBCZJMVYJEJOSDOBNBUVTWKBEHYNTZTJDBNMJRHVUJJYFRWY")
