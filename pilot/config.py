# config.py
# Labeling Instructions in Blocks

UNIVERSAL = """You will be given a set of codes with components of definitions of antisemitism.
You will be given a text with a unique comment_id and codes with unique code_ids.
The codes given describe definitions of what {ISorisNOT} antisemitic.
You will label the comment_id across each code.
You will return ONLY a JSON object in the following format:
{{"comment_id": [["code_id", "label"], ["code_id", "label"]]}}

Return one array per code given. Return nothing else.
Such that for the comment_id there is one tuple per code given,
where the code_id is the identifier string (e.g. A1NAME).

Response scale:

N — Not Applicable: The code is unambiguously inapplicable to the text.
    Example: "Political polarization is growing in the US." or "Pizza is my favorite." or "The conspiracy theory that Jews control the media is a common far-right trope."
    The text is completely unrelated or inapplicable to the code. This includes texts that critically discuss, quote, refute, or reference antisemitic ideas in an unambiguously neutral way.

E — Explicitly Applicable: There is direct and unambiguous evidence the code applies to the text. The text does not attempt to obfuscate its stance, and the code applies stably independent of context.
    Example: "I hate Jews."
    The text directly states its stance without any ambiguity.

I — Implicitly Applicable: There is strong evidence that the code applies to the text. The text communicates this through coded language, dogwhistles, numeric or symbolic encoding, or qualifying information contained within the text itself, such that the meaning is resolvable from the text alone, even though it is not stated plainly.
    Example: "(((They))) are always responsible" or "From the river to the sea, every last one of X must go" or "271k" referencing Holocaust-denial minimization.
    The text supplies everything needed to resolve the meaning, it is simply communicated through a device (parentheses, an internal qualifying clause, a known coded dogwhistle) rather than stated outright.

A — Ambiguous: It is unclear whether the code applies to the text, because the text does not supply the information needed to resolve it, even when accounting for coded language or devices the reader might recognize.
    Example: "They have always controlled the narrative" when 'They' has no clear target, or "Globalists are ruining everything" with no qualifying information present, or "From the river to the sea" without a clear target as-such.
    Nothing in the text, whether stated plainly or encoded, resolves the necessary meaning. This differs from I in that I requires the resolving information to be present somewhere in the text, even if disguised; A applies when that resolving information simply isn't there. Vague language alone does not mean a text is ambiguous if the text itself supplies the needed referent elsewhere.
"""

# ====================== IHRA

I_1 = """
   1.1 D1
   - D1PERCEPTION "Antisemitism is a certain perception of Jews"
   - D1HATE "which may be expressed as hatred toward Jews."
   - D1MANIFEST "Rhetorical and physical manifestations of antisemitism are directed toward Jewish or non-Jewish individuals and/or their property, toward Jewish community institutions and religious facilities."

   1.2 D2
   - D2ISRAELTARGET "Manifestations might include the targeting of the state of Israel, conceived as a Jewish collectivity."
   - D2CONSPIRACY "Antisemitism frequently charges Jews with conspiring to harm humanity"
   - D2COLLECTIVEBLAME "it is often used to blame Jews for 'why things go wrong.'"
   - D2STEREOTYPE "employs sinister stereotypes and negative character traits."
"""

# ----------------------

I_2 = """
   2.1 E1
   - E1VIOLENCE "Calling for, aiding, or justifying the killing or harming of Jews"
   - E1RADICAL "in the name of a radical ideology or an extremist view of religion."

   2.2 E2
   - E2ALLEGATION "Making mendacious ... allegations about Jews as such"
   - E2DEHUMANIZATION "dehumanizing ... allegations about Jews as such"
   - E2DEMONIZE "demonizing ... allegations about Jews as such"
   - E2STEREOTYPE "stereotypical allegations about Jews as such"
   - E2COLLECTIVEPOWER "the power of Jews as collective"
   - E2CONSPIRACY "the myth about a world Jewish conspiracy"
   - E2CONTROLMEDIA "Jews controlling the media"
   - E2CONTROLECONOMY "Jews controlling the economy"
   - E2CONTROLGOV "Jews controlling the government"
   - E2CONTROLOTHER "Jews controlling other societal institutions."

   2.3 E3
   - E3COLLECTIVEBLAME "Accusing Jews as a people of being responsible for real or imagined wrongdoing committed by a single Jewish person or group, or even for acts committed by non-Jews."
"""

# ----------------------

I_3 = """
   2.4 E4
   - E4HOLOCAUSTDENIAL "Denying the fact ... of the genocide of the Jewish people"
   - E4HOLOCAUSTMINIMIZE "Denying the ... scope ... of the genocide of the Jewish people"
   - E4HOLOCAUSTMECHANISM "Denying the ... mechanisms (e.g. gas chambers) ... of the genocide of the Jewish people"
   - E4HOLOCAUSTINTENT "Denying the ... intentionality of the genocide of the Jewish people"

   2.5 E5
   - E5HOLOCAUSTINVENT "Accusing the Jews as a people, or Israel as a state, of inventing ... the Holocaust."
   - E5HOLOCAUSTEXAGGERATE "Accusing the Jews as a people, or Israel as a state, of ... exaggerating the Holocaust."
"""

# ----------------------

I_4 = """
   2.6 E6
   - E6ISRAELLOYALTY "Accusing Jewish citizens of being more loyal to Israel"
   - E6GLOBALLOYALTY "or to the alleged priorities of Jews worldwide"

   2.7 E7
   - E7JEWISHRIGHTS "Denying the Jewish people their right to self-determination"
   - E7ISRAELRACIST "claiming that the existence of a State of Israel is a racist endeavor."

   2.8 E8
   - E8DOUBLESTANDARD "Applying double standards"
   - E8UNIQUEDEMAND "requiring of it a behavior not expected or demanded of any other democratic nation."

   2.9 E9
   - E9CLASSICSYMBOL "Using the symbols and images associated with classic antisemitism"
   - E9JESUSKILLING "claims of Jews killing Jesus"
   - E9BLOODLIBEL "blood libel"
   - E9CHARACTERIZEISRAEL "Using the symbols and images associated with classic antisemitism (e.g., claims of Jews killing Jesus or blood libel) to characterize Israel or Israelis."

   2.10 E10
   - E10ISRAELNAZI "Drawing comparisons of contemporary Israeli policy to that of the Nazis."

   2.11 E11
   - E11COLLECTIVEBLAME "Holding Jews collectively responsible for actions of the state of Israel."
"""

# ----------------------

I_5 = """
   3.1 E12
   - E12CRIMINAL "Antisemitic acts are criminal when they are so defined by law"
   - E12CRIMINALDENIAL "for example, denial of the Holocaust"
   - E12CRIMINALMATERIAL "or distribution of antisemitic materials in some countries."

   3.2 E13
   - E13TARGET "Criminal acts are antisemitic when the targets of attacks ... are selected because they are, or are perceived to be, Jewish or linked to Jews."
   - E13PEOPLE "whether they are people"
   - E13PROPERTY "or property"
   - E13BUILDINGS "such as buildings"
   - E13SCHOOLS "schools"
   - E13WORSHIP "places of worship"
   - E13CEMETERIES "cemeteries"

   3.3 E14
   - E14DISCRIMINATION "Antisemitic discrimination is the denial to Jews of opportunities or services available to others"
"""

# ----------------------

I_NO_1 = """
   - D2DOUBLESTANDARD "criticism of Israel similar to that leveled against any other country cannot be regarded as antisemitic."
"""

# ====================== Nexus

N_1 = """
   1.1 N1
   - N1BELIEFS "anti-Jewish beliefs, attitudes, actions or systemic conditions"
   - N1NEGATIVEATTITUDE "negative beliefs and feelings about Jews"
   - N1HOSTILECONDUCT "hostile behavior directed against Jews (because they are Jews)"
   - N1DISCRIMINATION "conditions that discriminate against Jews and significantly impede their ability to participate as equals in political, religious, cultural, economic, or social life."
"""

# ----------------------

N_2 = """
   2.1 N2
   - N2CONSPIRACY "Characterizing Israel as being part of a sinister world conspiracy of Jewish control of the media, economy, government or other financial, cultural or societal institutions."
   - N2CONTROLMEDIA "Jews controlling the media"
   - N2CONTROLECONOMY "Jews controlling the economy"
   - N2CONTROLGOV "Jews controlling the government"
   - N2CONTROLOTHER "Jews controlling other financial, cultural or societal institutions."

   2.2 N3
   - N3COLLECTIVEBLAME "Holding individuals or institutions, because they are Jewish, a priori culpable of real or imagined wrongdoing committed by Israel."

   2.3 N4
   - N4HIDDENCONSPIRACY "Indiscriminately blaming suffering and injustices around the world on a hidden Jewish conspiracy"
   - N4ISRAELHAND "or of being the maligning hand of Israel or Zionism."

   2.4 N5
   - N5LOYALTY "Considering Jews to be a priori incapable of setting aside their loyalty to the Jewish people and/or Israel."

   2.5 N6
   - N6IDENTITYDENY "Denigrating or denying the Jewish identity of certain Jews because they are perceived as holding the 'wrong' position (whether too critical or too favorable) on Israel."

   2.6 N7
   - N7COLLECTIVEGUILT "using symbols and images that present all Jews as collectively guilty for the actions of the State of Israel."

   2.7 N8
   - N8VIOLENCE "attacking and/or physically harming a Jew because of her/his relationship to Israel."

   2.8 N9
   - N9INCITEMENT "conveying intense hostility toward Jews who are connected to Israel in a way that intentionally or irresponsibly... provokes antisemitic violence."

   2.9 N10
   - N10SELFDETERMINATION "treating Israel in a negative manner based on a claim that Jews alone should be denied the right to define themselves as a people and to exercise any form of self-determination."

   2.10 N11
   - N11JEWISHRIGHTSDEFINE "advocating a political solution that denies Jews the right to define themselves as a people"
   - N11SELFDETERMINATION "denying them — because they are Jews — the right to self-determination"
   - N11JEWISHRIGHTS "and/or the right to physical safety and full human, civil, and religious rights."

   2.11 N12
   - N12DOUBLESTANDARD "treating Israel differently solely because it is a Jewish state, using standards different than those applied to other countries."
"""

# ----------------------

N_NO_1 = """
   3.1 N13
   - N13ISRAELCRITICISM "criticism of Zionism and Israel, opposition to Israel's policies, or nonviolent political action directed at the State of Israel and/or its policies should not, as such, be deemed antisemitic."

   3.2 N14
   - N14SUPPRESSIONFREEDOM "Using accusations of antisemitism as a tool to suppress criticism of Israel infringes on the principle of freedom of expression"
   - N14SUPPRESSIONDIALOGUE "and militates against constructive dialogue and debate among people with differing opinions."

   3.3 N15
   - N15HARSHCRITICISM "Even contentious, strident, or harsh criticism of Israel for its policies and actions, including those that led to the creation of Israel, is not per se illegitimate or antisemitic."

   3.4 N16
   - N16OPPOSITION "Opposition to Zionism and/or Israel does not necessarily reflect specific anti-Jewish animus nor purposefully lead to antisemitic behaviors and conditions."
   - N16NATIONALISM "opposing the principle of nationalism or ethnonationalist ideology"
   - N16ADVERSEEXPERIENCE "someone's personal or national experience may have been adversely affected by the creation of the State of Israel."

   3.5 N17
   - N17DISPROPORTIONATE "Paying disproportionate attention to Israel and treating Israel differently than other countries is not prima facie proof of antisemitism."
"""

# ====================== JDA

J_1 = """
   1.1 A1
   - A1ESSENTIAL
     "It is racist to essentialize (treat a character trait as inherent) or to make sweeping negative generalizations about a given population."

   1.2 A2
   - A2EVIL
     "Jews are linked to the forces of evil."
   - A2CONSPIRACY
     "the idea of a Jewish conspiracy"
   - A2HIDDENPOWER
     "\"the Jews\" possess hidden power"
   - A2COLLECTIVEAGENDA
     "promote their own collective agenda at the expense of other people."
   - A2CONTROLGOV
     "\"the Jews\" control governments with a \"hidden hand\""
   - A2CONTROLBANKS
     "own the banks"
   - A2CONTROLMEDIA
     "control the media"
   - A2LOYALTY
     "act as \"a state within a state\""
   - A2DISEASE
     "responsible for spreading disease (such as Covid-19)."

   1.3 A3
   - A3WEALTH
     "all Jews are wealthy"
   - A3STINGY
     "inherently stingy"
   - A3UNPATRIOTIC
     "or unpatriotic."
   - A3CARICATURE
     "depicted as grotesque, with big noses and associated with wealth."
   - A3VIOLENCE
     "assaulting someone because she or he is Jewish"
   - A3SYNAGOGUE
     "attacking a synagogue"
   - A3SWASTIKA
     "daubing swastikas on Jewish graves"
   - A3DISCRIMINATION
     "refusing to hire or promote people because they are Jewish."
"""

# ----------------------

J_2 = """
   1.4 A4
   - A4DOGWHISTLE
     "Antisemitism can be direct or indirect, explicit or coded."
   - A4ROTHSCHILD
     "\"the Rothschilds control the world\""
   - A4ISRAELEVIL
     "portraying Israel as the ultimate evil"
   - A4ISRAELINFLUENCE
     "grossly exaggerating its actual influence"

   1.5 A5
   - A5HOLOCAUSTDENIAL
     "Denying or minimizing the Holocaust by claiming that the deliberate Nazi genocide of the Jews did not take place"
   - A5HOLOCAUSTMECHANISM
     "there were no extermination camps or gas chambers"
   - A5HOLOCAUSTMINIMIZE
     "the number of victims was a fraction of the actual total"
"""

# ----------------------

J_3 = """
   2.1 B6
   - B6CHARACTERIZEISRAEL
     "Applying the symbols, images and negative stereotypes of classical antisemitism... to the State of Israel."

   2.2 B7
   - B7COLLECTIVEBLAME
     "Holding Jews collectively responsible for Israel’s conduct"
   - B7ISRAELAGENT
     "treating Jews, simply because they are Jewish, as agents of Israel."

   2.3 B8
   - B8FORCECONDEMN
     "Requiring people, because they are Jewish, publicly to condemn Israel or Zionism"

   2.4 B9
   - B9ISRAELLOYALTY
     "Assuming that non-Israeli Jews, simply because they are Jews, are necessarily more loyal to Israel than to their own countries."

   2.5 B10
   - B10JEWISHRIGHTS
     "Denying the right of Jews in the State of Israel to exist and flourish, collectively and individually, as Jews, in accordance with the principle of equality."
"""

# ----------------------

J_NO_1 = """
   3.1 C11
   - C11PALESTINIANJUSTICE
     "Supporting the Palestinian demand for justice"
   - C11PALESTINIANRIGHTS
     "the full grant of their political, national, civil, and human rights, as encapsulated in international law."

   3.2 C12
   - C12ZIONCRITICAL
     "Criticizing or opposing Zionism as a form of nationalism"
   - C12SOLUTIONS
     "arguing for a variety of constitutional arrangements for Jews and Palestinians... whether in two states, a binational state, unitary democratic state, federal state, or in whatever form."
   - C12EQUALRIGHTS
     "support arrangements that accord full equality to all inhabitants \"between the river and the sea\""

   3.3 C13
   - C13ISRAELEVIDENCE
     "Evidence-based criticism of Israel as a state."
   - C13ISRAELINSTITUTIONS
     "its institutions and founding principles."
   - C13ISRAELPOLICIES
     "its policies and practices, domestic and abroad"
   - C13ISRAELOPT
     "the conduct of Israel in the West Bank and Gaza"
   - C13ISRAELREGION
     "the role Israel plays in the region"
   - C13ISRAELDISCRIMINATION
     "It is not antisemitic to point out systematic racial discrimination."
   - C13ISRAELNORMS
     "the same norms of debate that apply to other states"
   - C13ISRAELCOMPARE
     "to compare Israel with other historical cases, including settler-colonialism or apartheid."

   3.4 C14
   - C14BDS
     "Boycott, divestment and sanctions are commonplace, non-violent forms of political protest against states. In the Israeli case they are not, in and of themselves, antisemitic."

   3.5 C15
   - C15REASONABLE
     "Political speech does not have to be measured, proportional, tempered, or reasonable... the line between antisemitic and non-antisemitic speech is different from the line between unreasonable and reasonable speech.""
   - C15DOUBLESTANDARD
     "Criticism that some may see as excessive or contentious, or as reflecting a \"double standard\", is not, in and of itself, antisemitic."
"""

# ====================== Input

INPUT = """

This is the comment_id: {id}
This is the text to code: {text}

The key-value pair with the labels is:
"""

