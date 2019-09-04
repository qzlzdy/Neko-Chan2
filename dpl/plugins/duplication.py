from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    context = session.msg
    if context == '':
        context = ' '
    return IntentCommand(90.0,'duplicate', current_arg=context)

@on_command('duplicate')
async def duplicate(session: CommandSession):
    context = session.get('context')
    await session.send(context)

@duplicate.args_parser
async def _(session: CommandSession):
    session.state['context'] = session.current_arg
