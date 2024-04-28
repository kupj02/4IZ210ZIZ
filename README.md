# Analýza modelu predikce mrtvice

## Přehled
Tento repozitář popisuje naše přístupy k zlepšení výsledků zdravotní péče prostřednictvím předpovědi rizika mrtvice. Cílem je umožnit preventivní opatření, snížit náklady na zdravotní péči a poskytnout personalizovanou péči pacientům prostřednictvím prediktivního modelování.

## Hodnota pro byznys

### Zlepšení výsledků zdravotní péče
- **Včasná předpověď rizika mrtvice** může vést k preventivním opatřením, která sníží výskyt mrtvice, zlepší výsledky pacientů a zároveň sníží zátěž zdravotnických pracovišť a systémů.

### Snížení nákladů
- **Léčba mrtvice** je nákladná, zejména pokud je nutná dlouhodobá rehabilitace. Prediktivní modely mohou pomoci při efektivnějším rozdělování zdrojů zdravotní péče a zaměřit se na prevenci u vysoce rizikových pacientů, aby se předešlo pozdějším nákladným zákrokům.

### Personalizovaná péče o pacienty
- **Díky identifikaci rizikových jedinců** mohou poskytovatelé zdravotní péče nabízet personalizované zdravotní plány, včetně úpravy životního stylu a předepsání léků, s cílem zmírnit riziko mrtvice.

## Vybrané přizpůsobení

### Cílový atribut
- Atribut "stroke" v datovém souboru, což je binární hodnota (1 znamená, že jedinec prodělal mrtvici, 0 znamená, že neprodělal).

### Instance zájmu
- Osoba s ID 9046 s atributy, jako jsou pohlaví, věk, hypertenze, srdeční onemocnění, manželský stav, typ práce, typ bydliště, průměrná hladina glukózy, BMI a stav kouření.

### Atribut zájmu
- Osoby s BMI nad úrovní 25.

### Podskupina zájmů
- Zaměření na demografickou skupinu s vyšším rizikem, jako jsou starší pacienti, jedinci s rodinnou anamnézou mozkové příhody nebo ti, kteří již mají nějaké onemocnění, například cukrovku nebo hypertenzi.

## Matice nákladů
- Vyšší sankce za falešně negativní výsledky ve srovnání s falešně pozitivními výsledky, z důvodu výrazně vyšších nákladů na zdravotní péči při nepředpovězení mrtvice.

## Prozkoumání dat
Podrobnosti o analýze dat, která zahrnují vliv různých proměnných na riziko infarktu, s důrazem na věk a BMI jako potenciální rizikové faktory.

## Předzpracování dat
Popis kroků předzpracování dat, včetně rozdělení dat, odstranění chybějících hodnot a normalizace numerických proměnných.

## Modelování
Detaily o použití modelů rozhodovacích stromů a náhodných lesů, včetně tuningování hyperparametrů a hodnocení modelů.

## Závěr
Sumarizace výsledků a rozhodnutí o nejlepším modelu na základě dosažené přesnosti a robustnosti.



