# ChatWP

`ChatWP` is an AI-powered software to interact with your WordPress site.

## Usage

### Set environment variables

ChatWP supposes the environment variables below are set:

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
Question: 中村勘九郎の芝居のうち、このブログの著者が観劇したのは何？
Answer:
中村勘九郎の芝居のうち、このブログの著者が観劇したのは「夏祭浪花鑑」である。URL: https://kentarokuribayashi.com/journal/2021/05/23/2021%e5%b9%b45%e6%9c%8823%e6%97%a5
```

## Author

Kentaro Kuribayashi <kentarok@gmail.com>

