exports.run = async (client, message, args) => {
    await message.channel.send('Pong!').catch(console.error)
        .then( (msg) => {
            let ms = Math.abs(message.createdTimestamp - msg.createdTimestamp);
            msg.edit(`Pong! ~ Took ${ms}ms`);
        });
};

exports.help = {
    name: 'ping'
};