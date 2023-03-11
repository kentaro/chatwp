# ChatWP

`ChatWP` is an AI-powered software to interact with WordPress sites. It pretends as if it were the author of the site.

## Usage

### Set environment variables

`ChatWP` supposes the environment variables below are set:

- `OPEN_API_KEY`: Your API Key for Open AI
- `WORDPRESS_URL`: The URL of your WordPress installation
- `WORDPRESS_USERNAME`: Your username of the WordPress site
- `WORDPRESS_PASSWORD`: Application password for the Wordpress site (see  [How to Create an Application Password for WordPress](https://www.paidmembershipspro.com/create-application-password-wordpress/) for details)

### Install prerequisites

```sh
pip install -r requirements.txt
```

### Make index

```shell
python ./make_index.py
```

It may take a long time that depends on how many articles your WordPress site has.

Here's the result for my WordPress site which has 5,000+ articles.

```sh
time python ./make_index.py
INFO:root:> [build_index_from_documents] Total LLM token usage: 0 tokens
INFO:root:> [build_index_from_documents] Total embedding token usage: 4752468 tokens

________________________________________________________
Executed in   25.12 mins    fish           external
   usr time   81.14 secs    0.09 millis   81.13 secs
   sys time    9.29 secs    1.04 millis    9.29 secs
```

### Chat with your WordPress site

```shell
python ./chatwp.py
Question:
```

## Examples

These examples are based on [my blog](https://kentarokuribayashi.com/).

```
Question: 好きな本はなんですか？
Answer: 私の好きな本は、小説や批評的な文章が多いですが、原初的な感覚的なレベルである言葉の響き、つらなり、字面などにも興味があります。例えば、「本好きへの 100 の質問」への回答 (https://kentarokuribayashi.com/journal/2003/02/19/20030219-1045662426) でも述べたように、本にしかないコンテンツがある以上、重要な情報源でありつづけると思っています。
```

```
Question: Elixirの特徴は？
Answer: Elixirは、安全で拡張性の高いプログラミング言語です。安全性は、関数型プログラミングの考え方を採用していることにより、プログラムのバグを減らすことができます。また、拡張性の高さは、Erlang VM上で動作することにより、高い並行性を実現しています。詳しくは、『プログラミングElixir 第2版』のURL（https://kentarokuribayashi.com/journal/2020/12/14/programming-elixir-1-6-ja）をご覧ください。
```

```
Question: マネジメントにおいて大切なことはなんですか？
Answer:
マネジメントにおいて大切なことは、業績を伸ばすためだけでなく、チームメンバーの成長を促進することです。マネジメントの目的とする業績の向上と、マネジメントそのものについての知見をきっちり区別し、多種多様なテクニックを習得し、適用することが重要です。先達の経験や書籍からの知見を獲得し、知識とスキルを向上させ、自らの経験と得た知見を一般化・抽象化して理論・テクニックにすることも重要です。(Source: https://kentarokuribayashi.com/journal/2016/12/23/2016-12-23-113829)
```

```
Question: 社会人大学院生は楽しいですか？
Answer:
社会人大学院生は楽しいですが、苦労も多いです。自分が本当にやりたいことを見つめ、しかし単に自分の興味関心だけでなく、アカデミズムにおける基準に従って自己の成果を判定し、さらには社会にとって役立つような新しい何かを生み出すことを目指すことは、ストレスフルな状況であるとは思います。しかし、それでも生きる上での課題の解決はできますし、ひとの役に立つこともたまにはあるでしょう。社会人大学院生は楽しいですが、苦労も多いです。(Source: https://kentarokuribayashi.com/journal/2020/12/03/adult-student-2020)
```

## Author

Kentaro Kuribayashi &lt;kentarok@gmail.com&gt;
