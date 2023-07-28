from invoke import task


@task
def deploy(ctx):
    ctx.run("cd deploy && python deploy.py")
