import zmail
mail_content={
    "subject":"邮件主题",
    "content_text":"征文"
}
serve=zmail.server("lhxpdy@qq.com","ommoavuyswqubbaf")
serve.send_mail("487454153@qq.com",mail_content)
