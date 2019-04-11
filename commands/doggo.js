const { RichEmbed} = require('discord.js');
const fetch = require('node-fetch');

exports.run = async (client, message, args) => {

    let doggo = await fetch ('https://dog.ceo/api/breeds/image/random')
        .then(res => res.json())
        .then(json => json.message);

    let embed = new RichEmbed()
        .setAuthor(message.member.user.tag, message.member.user.avatarURL)
        .setColor(0x54dd23)
        .setImage(doggo)
        .setFooter('A random doggo!');

    message.channel.send(embed);
};

exports.help = {
    name: 'kot'
};