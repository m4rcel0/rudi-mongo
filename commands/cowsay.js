const { RichEmbed } = require('discord.js');
const cowsay  = require('cowsay');

exports.run = (client, message, args) => {

    // No message provided
    if (!args.length) return message.channel.send("Usage: !cowsay 'message'");
    
    // Converts the args array into a string, and word-wraps to 40 chars
    // Word-wrap credit: https://stackoverflow.com/a/51506718
    let cowtext = args.join(" ").replace(/(?![^\n]{1,40}$)([^\n]{1,40})\s/g, '$1\n');

    let cowmsg = cowsay.say({
        text: cowtext
    });

    if (cowmsg.length > 2000) {
        cowmsg = cowsay.say({
            text: "The message is too big, I can't handle all that much",
            e: "XX",
            T: "U "
        });
    };

    let embed = new RichEmbed()
        .setAuthor(message.member.user.tag, message.member.user.avatarURL)
        .setColor(0x2dc9c8)
        .setDescription(` \`\`\`${cowmsg}\`\`\` `)

    message.channel.send(embed);
};

exports.help = {
    name: 'cowsay'
};