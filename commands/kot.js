const { RichEmbed} = require('discord.js');
const fetch = require('node-fetch');

exports.run = async (client, message, args) => {

    let kot = await fetch ('http://aws.random.cat/meow')
        .then(res => res.json())
        .then(json => json.file);

    let embed = new RichEmbed()
        .setAuthor(message.member.user.tag, message.member.user.avatarURL)
        .setColor(0x54dd23)
        .setImage(kot)
        .setFooter('A random kot!');

    message.channel.send(embed);
};

exports.help = {
    name: 'kot'
};