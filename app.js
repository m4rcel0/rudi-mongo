const Discord = require('discord.js');
const fs = require('fs');
const Enmap = require('enmap');
require('dotenv-flow').config();
const client = new Discord.Client();
client.commands = new Enmap();

//Loads all events at startup
fs.readdir('./events/', (err, files) => {
    if (err) return console.error;
    files.forEach(file => {
        if (!file.endsWith('.js')) return;
        const evt = require(`./events/${file}`);
        let evtName = file.split('.')[0];
        console.log(`Loaded '${evtName}'.`);
        client.on(evtName, evt.bind(null, client));
    });
});

//Loads all commands at startup
fs.readdir('./commands/', async(err, files) => {
    if (err) return console.error;
    files.forEach(file =>{
        if (!file.endsWith('.js')) return;
        let props = require(`./commands/${file}`);
        let cmdName = file.split('.')[0];
        console.log(`Loaded command '${cmdName}'.`);
        client.commands.set(cmdName, props);
    
    });
});

client.login();