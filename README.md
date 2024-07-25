アンジャッシュのアルバム型コントの自動生成に用いるコードです。

#用語集

Normal Position Fact   : インスタンス化されたオブジェクトの各アトリビュートに入った、普通の情報。
                         dog.sales_unit = None
                         meat_sales.unit = ["pound", "kcal"]
                         alcohol_drink.shortage_timing = ["the prohibition era"]
                         sanitiser.shortage_timing = ["the pandemic"]
Normal Position Speech : Normal Position Factを用いた普通の文。
                         "I bought a dog"
                         "I bought 5 pounds of meat."
                         "During the prohibition era, there was a shortage of alcohol drinks."
                         "During the pandemic, there was a shortage of sanitiser."
Repositioner           : 異常行為を to treat {A} as {B} や to treat {A} as inferior to {B} や to treat {A} as {B} rather than {C} のような文にしたもの。ジョークを暗号として見た時の平文に相当する。
                         to treat dog as meat
                         to treat sanitiser as alcohol drink
Repositioned Speech    : Repositionerに則り、Normal Position Speech 内の Normal Position Fact を置換したもの。
                         "I bought 5 pounds of dog."
                         "During the prohibition era, there was a shortage of sanitiser."
Hidden Position Speech : アルバム型コントにおいては、実際に登場人物が Repositioner および Repositioned Speech を実行しているわけではない。その旨を明示するために一部のプレースホルダをあいまいな表現(=誤解を解消しない表現)に置き換えた Repositioned Speechを指す。
                         "I bought 5 pounds of it."
                         "During the prohibition era, there was a shortage of it."
                         
