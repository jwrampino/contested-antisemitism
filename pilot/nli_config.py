# nli_config.py

# Grammatically complete hypotheses for all 127 codes, for NLI scoring.

# exemplar: 0 -> "This text expresses: {}."      (propositional/belief content)
#           1 -> "This text is an example of: {}." (act/category description)


CODE_HYPOTHESES = {
    # ====================== IHRA D1/D2
    "D1PERCEPTION": ("a certain perception of Jews", 0),
    "D1HATE": ("hatred toward Jews", 0),
    "D1MANIFEST": ("rhetorical and physical manifestations of antisemitism directed toward Jewish or non-Jewish individuals and/or their property, toward Jewish community institutions and religious facilities", 1),
    "D2ISRAELTARGET": ("the targeting of the state of Israel, conceived as a Jewish collectivity", 1),
    "D2CONSPIRACY": ("charging Jews with conspiring to harm humanity", 1),
    "D2COLLECTIVEBLAME": ("blaming Jews for \"why things go wrong\"", 1),
    "D2STEREOTYPE": ("sinister stereotypes and negative character traits about Jews", 0),
    "D2DOUBLESTANDARD": ("criticism of Israel similar to that leveled against any other country", 0),

    # ====================== IHRA E1-E3
    "E1VIOLENCE": ("calling for, aiding, or justifying the killing or harming of Jews", 1),
    "E1RADICAL": ("calling for, aiding, or justifying the killing or harming of Jews in the name of a radical ideology or an extremist view of religion", 1),
    "E2ALLEGATION": ("making mendacious allegations about Jews as such", 1),
    "E2DEHUMANIZATION": ("making dehumanizing allegations about Jews as such", 1),
    "E2DEMONIZE": ("making demonizing allegations about Jews as such", 1),
    "E2STEREOTYPE": ("making stereotypical allegations about Jews as such", 1),
    "E2COLLECTIVEPOWER": ("allegations about the power of Jews as a collective", 0),
    "E2CONSPIRACY": ("the myth about a world Jewish conspiracy", 0),
    "E2CONTROLMEDIA": ("Jews controlling the media", 0),
    "E2CONTROLECONOMY": ("Jews controlling the economy", 0),
    "E2CONTROLGOV": ("Jews controlling the government", 0),
    "E2CONTROLOTHER": ("Jews controlling other societal institutions", 0),
    "E3COLLECTIVEBLAME": ("accusing Jews as a people of being responsible for real or imagined wrongdoing committed by a single Jewish person or group, or even for acts committed by non-Jews", 1),

    # ====================== IHRA E4-E5
    "E4HOLOCAUSTDENIAL": ("denying the fact of the genocide of the Jewish people", 1),
    "E4HOLOCAUSTMINIMIZE": ("denying the scope of the genocide of the Jewish people", 1),
    "E4HOLOCAUSTMECHANISM": ("denying the mechanisms (e.g. gas chambers) of the genocide of the Jewish people", 1),
    "E4HOLOCAUSTINTENT": ("denying the intentionality of the genocide of the Jewish people", 1),
    "E5HOLOCAUSTINVENT": ("accusing the Jews as a people, or Israel as a state, of inventing the Holocaust", 1),
    "E5HOLOCAUSTEXAGGERATE": ("accusing the Jews as a people, or Israel as a state, of exaggerating the Holocaust", 1),

    # ====================== IHRA E6-E9
    "E6ISRAELLOYALTY": ("accusing Jewish citizens of being more loyal to Israel", 1),
    "E6GLOBALLOYALTY": ("accusing Jewish citizens of being more loyal to the alleged priorities of Jews worldwide", 1),
    "E7JEWISHRIGHTS": ("denying the Jewish people their right to self-determination", 1),
    "E7ISRAELRACIST": ("claiming that the existence of a State of Israel is a racist endeavor", 1),
    "E8DOUBLESTANDARD": ("applying double standards to Israel", 1),
    "E8UNIQUEDEMAND": ("requiring of Israel a behavior not expected or demanded of any other democratic nation", 1),
    "E9CLASSICSYMBOL": ("using the symbols and images associated with classic antisemitism", 1),
    "E9JESUSKILLING": ("claims of Jews killing Jesus", 1),
    "E9BLOODLIBEL": ("blood libel", 1),
    "E9CHARACTERIZEISRAEL": ("using the symbols and images associated with classic antisemitism (e.g., claims of Jews killing Jesus or blood libel) to characterize Israel or Israelis", 1),

    # ====================== IHRA E10-E11
    "E10ISRAELNAZI": ("drawing comparisons of contemporary Israeli policy to that of the Nazis", 1),
    "E11COLLECTIVEBLAME": ("holding Jews collectively responsible for actions of the state of Israel", 1),

    # ====================== IHRA E12-E14
    "E12CRIMINAL": ("antisemitic acts that are criminal when so defined by law", 1),
    "E12CRIMINALDENIAL": ("denial of the Holocaust as a criminal antisemitic act", 1),
    "E12CRIMINALMATERIAL": ("distribution of antisemitic materials as a criminal antisemitic act", 1),
    "E13TARGET": ("criminal acts where the targets of attacks are selected because they are, or are perceived to be, Jewish or linked to Jews", 1),
    "E13PEOPLE": ("criminal acts targeting people because they are, or are perceived to be, Jewish or linked to Jews", 1),
    "E13PROPERTY": ("criminal acts targeting property because it is, or is perceived to be, Jewish or linked to Jews", 1),
    "E13BUILDINGS": ("criminal acts targeting Jewish buildings", 1),
    "E13SCHOOLS": ("criminal acts targeting Jewish schools", 1),
    "E13WORSHIP": ("criminal acts targeting Jewish places of worship", 1),
    "E13CEMETERIES": ("criminal acts targeting Jewish cemeteries", 1),
    "E14DISCRIMINATION": ("the denial to Jews of opportunities or services available to others", 1),

    # ====================== Nexus N1
    "N1BELIEFS": ("anti-Jewish beliefs, attitudes, actions or systemic conditions", 0),
    "N1NEGATIVEATTITUDE": ("negative beliefs and feelings about Jews", 0),
    "N1HOSTILECONDUCT": ("hostile behavior directed against Jews (because they are Jews)", 1),
    "N1DISCRIMINATION": ("conditions that discriminate against Jews and significantly impede their ability to participate as equals in political, religious, cultural, economic, or social life", 1),

    # ====================== Nexus N2-N12
    "N2CONSPIRACY": ("characterizing Israel as being part of a sinister world conspiracy of Jewish control of the media, economy, government or other financial, cultural or societal institutions", 1),
    "N2CONTROLMEDIA": ("Jews controlling the media", 0),
    "N2CONTROLECONOMY": ("Jews controlling the economy", 0),
    "N2CONTROLGOV": ("Jews controlling the government", 0),
    "N2CONTROLOTHER": ("Jews controlling other financial, cultural or societal institutions", 0),
    "N3COLLECTIVEBLAME": ("holding individuals or institutions, because they are Jewish, a priori culpable of real or imagined wrongdoing committed by Israel", 1),
    "N4HIDDENCONSPIRACY": ("indiscriminately blaming suffering and injustices around the world on a hidden Jewish conspiracy", 1),
    "N4ISRAELHAND": ("indiscriminately blaming suffering and injustices around the world on the maligning hand of Israel or Zionism", 1),
    "N5LOYALTY": ("considering Jews to be a priori incapable of setting aside their loyalty to the Jewish people and/or Israel", 1),
    "N6IDENTITYDENY": ("denigrating or denying the Jewish identity of certain Jews because they are perceived as holding the \"wrong\" position (whether too critical or too favorable) on Israel", 1),
    "N7COLLECTIVEGUILT": ("using symbols and images that present all Jews as collectively guilty for the actions of the State of Israel", 1),
    "N8VIOLENCE": ("attacking and/or physically harming a Jew because of her/his relationship to Israel", 1),
    "N9INCITEMENT": ("conveying intense hostility toward Jews who are connected to Israel in a way that intentionally or irresponsibly provokes antisemitic violence", 1),
    "N10SELFDETERMINATION": ("treating Israel in a negative manner based on a claim that Jews alone should be denied the right to define themselves as a people and to exercise any form of self-determination", 1),
    "N11JEWISHRIGHTSDEFINE": ("advocating a political solution that denies Jews the right to define themselves as a people", 1),
    "N11SELFDETERMINATION": ("denying Jews, because they are Jews, the right to self-determination", 1),
    "N11JEWISHRIGHTS": ("denying Jews, because they are Jews, the right to physical safety and full human, civil, and religious rights", 1),
    "N12DOUBLESTANDARD": ("treating Israel differently solely because it is a Jewish state, using standards different than those applied to other countries", 1),

    # ====================== Nexus N13-N17
    "N13ISRAELCRITICISM": ("criticism of Zionism and Israel, opposition to Israel's policies, or nonviolent political action directed at the State of Israel and/or its policies", 0),
    "N14SUPPRESSIONFREEDOM": ("using accusations of antisemitism as a tool to suppress criticism of Israel, infringing on the principle of freedom of expression", 1),
    "N14SUPPRESSIONDIALOGUE": ("using accusations of antisemitism as a tool to suppress criticism of Israel, militating against constructive dialogue and debate among people with differing opinions", 1),
    "N15HARSHCRITICISM": ("contentious, strident, or harsh criticism of Israel for its policies and actions, including those that led to the creation of Israel", 0),
    "N16OPPOSITION": ("opposition to Zionism and/or Israel not necessarily reflecting specific anti-Jewish animus or purposefully leading to antisemitic behaviors and conditions", 0),
    "N16NATIONALISM": ("opposing the principle of nationalism or ethnonationalist ideology", 1),
    "N16ADVERSEEXPERIENCE": ("someone's personal or national experience being adversely affected by the creation of the State of Israel", 0),
    "N17DISPROPORTIONATE": ("paying disproportionate attention to Israel and treating Israel differently than other countries", 1),

    # ====================== JDA A1-A3
    "A1ESSENTIAL": ("essentializing (treating a character trait as inherent) or making sweeping negative generalizations about a given population", 1),
    "A2EVIL": ("Jews are linked to the forces of evil", 0),
    "A2CONSPIRACY": ("the idea of a Jewish conspiracy", 0),
    "A2HIDDENPOWER": ("the Jews possess hidden power", 0),
    "A2COLLECTIVEAGENDA": ("Jews promote their own collective agenda at the expense of other people", 0),
    "A2CONTROLGOV": ("the Jews control governments with a hidden hand", 0),
    "A2CONTROLBANKS": ("Jews own the banks", 0),
    "A2CONTROLMEDIA": ("Jews control the media", 0),
    "A2LOYALTY": ("Jews act as \"a state within a state\"", 0),
    "A2DISEASE": ("Jews are responsible for spreading disease (such as Covid-19)", 0),
    "A3WEALTH": ("all Jews are wealthy", 0),
    "A3STINGY": ("all Jews are inherently stingy", 0),
    "A3UNPATRIOTIC": ("all Jews are unpatriotic", 0),
    "A3CARICATURE": ("Jews depicted as grotesque, with big noses and associated with wealth", 1),
    "A3VIOLENCE": ("assaulting someone because she or he is Jewish", 1),
    "A3SYNAGOGUE": ("attacking a synagogue", 1),
    "A3SWASTIKA": ("daubing swastikas on Jewish graves", 1),
    "A3DISCRIMINATION": ("refusing to hire or promote people because they are Jewish", 1),

    # ====================== JDA A4-A5
    "A4DOGWHISTLE": ("antisemitism that is direct or indirect, explicit or coded", 0),
    "A4ROTHSCHILD": ("the Rothschilds control the world", 0),
    "A4ISRAELEVIL": ("portraying Israel as the ultimate evil", 1),
    "A4ISRAELINFLUENCE": ("grossly exaggerating Israel's actual influence", 1),
    "A5HOLOCAUSTDENIAL": ("denying or minimizing the Holocaust by claiming that the deliberate Nazi genocide of the Jews did not take place", 1),
    "A5HOLOCAUSTMECHANISM": ("denying or minimizing the Holocaust by claiming there were no extermination camps or gas chambers", 1),
    "A5HOLOCAUSTMINIMIZE": ("denying or minimizing the Holocaust by claiming the number of victims was a fraction of the actual total", 1),

    # ====================== JDA B6-B10
    "B6CHARACTERIZEISRAEL": ("applying the symbols, images and negative stereotypes of classical antisemitism to the State of Israel", 1),
    "B7COLLECTIVEBLAME": ("holding Jews collectively responsible for Israel's conduct", 1),
    "B7ISRAELAGENT": ("treating Jews, simply because they are Jewish, as agents of Israel", 1),
    "B8FORCECONDEMN": ("requiring people, because they are Jewish, publicly to condemn Israel or Zionism", 1),
    "B9ISRAELLOYALTY": ("assuming that non-Israeli Jews, simply because they are Jews, are necessarily more loyal to Israel than to their own countries", 1),
    "B10JEWISHRIGHTS": ("denying the right of Jews in the State of Israel to exist and flourish, collectively and individually, as Jews, in accordance with the principle of equality", 1),

    # ====================== JDA C11-C15
    "C11PALESTINIANJUSTICE": ("supporting the Palestinian demand for justice", 1),
    "C11PALESTINIANRIGHTS": ("supporting the full grant of the Palestinian people's political, national, civil, and human rights, as encapsulated in international law", 1),
    "C12ZIONCRITICAL": ("criticizing or opposing Zionism as a form of nationalism", 1),
    "C12SOLUTIONS": ("arguing for a variety of constitutional arrangements for Jews and Palestinians, whether in two states, a binational state, unitary democratic state, federal state, or in whatever form", 1),
    "C12EQUALRIGHTS": ("supporting arrangements that accord full equality to all inhabitants between the river and the sea", 1),
    "C13ISRAELEVIDENCE": ("evidence-based criticism of Israel as a state", 0),
    "C13ISRAELINSTITUTIONS": ("evidence-based criticism of Israel's institutions and founding principles", 0),
    "C13ISRAELPOLICIES": ("evidence-based criticism of Israel's policies and practices, domestic and abroad", 0),
    "C13ISRAELOPT": ("evidence-based criticism of the conduct of Israel in the West Bank and Gaza", 0),
    "C13ISRAELREGION": ("evidence-based criticism of the role Israel plays in the region", 0),
    "C13ISRAELDISCRIMINATION": ("pointing out systematic racial discrimination", 1),
    "C13ISRAELNORMS": ("evidence-based criticism of Israel using the same norms of debate that apply to other states", 0),
    "C13ISRAELCOMPARE": ("evidence-based criticism comparing Israel with other historical cases, including settler-colonialism or apartheid", 0),
    "C14BDS": ("boycott, divestment and sanctions as commonplace, non-violent forms of political protest against Israel", 0),
    "C15REASONABLE": ("political speech that is not measured, proportional, tempered, or reasonable", 0),
    "C15DOUBLESTANDARD": ("criticism that some may see as excessive or contentious, or as reflecting a double standard", 0),
}

TEMPLATES = {
    0: "This text expresses: {}.",
    1: "This text is an example of: {}.",
}

def get_hypothesis(code_id):
    definition, exemplar = CODE_HYPOTHESES[code_id]
    return TEMPLATES[exemplar].format(definition)

def get_template(code_id):
    _, exemplar = CODE_HYPOTHESES[code_id]
    return TEMPLATES[exemplar]

print(f"{len(CODE_HYPOTHESES)} codes defined")
print(f"exemplar=0 (expresses): {sum(1 for _, e in CODE_HYPOTHESES.values() if e == 0)}")
print(f"exemplar=1 (is an example of): {sum(1 for _, e in CODE_HYPOTHESES.values() if e == 1)}")