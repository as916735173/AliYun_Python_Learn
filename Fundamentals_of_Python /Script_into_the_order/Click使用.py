import click


# 二、Click定义可选选项Option
# @click.command()
# @click.option('--count', default=1, type=int, help="you count")
# def hello(count):
#     click.echo(count)
#     click.echo("hello world !")
#
#
# if __name__ == '__main__':
#     hello()

# 三、Click定义参数Argument
@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def inout(input, output):
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)


# 四、Click接受的参数类型
# @click.command()
# @click.argument('action', type=str)
# @click.option('--ocount', type=int, default=1)
# def hello(action, ocount):
#     click.echo(action)
#     click.echo(ocount)
#     click.echo('hello world !')


# if __name__ == '__main__':
#     hello()


# 五、Click获取用户输入Prompt
@click.command()
def hello():
    count = click.prompt('please input a int', type=int)
    click.echo(count)
    click.echo("hello world !")
    if click.confirm('Do you want to continue ?'):
        click.echo("done")


if __name__ == '__main__':
    hello()
