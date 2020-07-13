# snapshot2.0

Demo project to manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the config file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional