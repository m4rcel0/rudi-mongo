exports.run = async (client, message, args) => {
    await message.channel.send('Pong!').catch(console.error)
        .then( (pong) => {
            let time = pong.createdTimestamp - message.createdTimestamp;
            pong.edit(`Pong! ~ Took ${time}ms`);
        });
};

exports.help = {
    name: 'ping'
};