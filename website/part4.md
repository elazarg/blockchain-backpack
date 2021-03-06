---
title: "The Trade-offs Being Made"
layout: page
prev-page:
    title: "Trading"
    url: part3.html
next-page:
    title: "Statistics"
    url: part5.html
---

The Trade-offs Being Made
-------------------------

In Part 1, I talked about how everyone should be at least as well off under a new proposed system as they would be under the old one. I assert that Valve would be better off under this system than they are now, but we need to be clear about what trade-offs are involved here. Valve would be trading the ability to make arbitrary changes to the item database for increased security. This is a beneficial trade off.

And there are constant security problems. A few months ago, there was [some sort of remote code execution attack][cssrc] against an older version of CounterStrike. The game client wasn't hardened, and malicious servers sent exploits to clients. Once the attackers had control of a user's computer, they stole all valuable items. More recently, the vulnerability of the week was a remote code execution bug in [TeamSpeak][], a third party voice communication program used by competitive players.

A user can do everything correctly and still have their items stolen due to a zero day in a program they use. It's worth trading a bit of flexibility to bolster security when theft is so rampant, as a system that users don't trust is a system that won't be used.

### The Upsides

These attacks happen because having access to a user's computer is all you need to steal their items. Installing a remote control trojan gives you access to a user's logged in Steam interface. Since most users stay logged in to their webmail, the trade confirmation emails will only stop purely automated attacks. From a security standpoint, the user's machine can't be trusted. Just because a logged in Steam client sends a command doesn't mean that the user initiated that command.

Valve appears to have realized this as they've just announced that people who use a smartphone for two-factor authentication will need to provide an authentication code from their phone on every trade they make. This is a massive improvement over the status quo, but not everyone has a smartphone, and it's not like the [security story on Android is much better than Windows][android].

Contrast this with the system I'm proposing, using dedicated [Trezor][trezor]-like hardware for signing digital transactions. Single purpose devices can be manufactured extremely cheaply and are more secure because they don't have the attack surface of a general purpose computer. They can even be used to prevent attacks on compromised machines. An attacker who has taken over a user's computer can cause the steam client to generate a command to perform a malicious trade, but said trade would be displayed on the screen of the signing hardware. To actually perform the trade, the user would have to press a button on the signing hardware. This makes large classes of current attacks impossible, which lowers Valve's support costs and stops the inflation caused by Steam Support duped items.

Furthermore, increased security makes people feel better about spending money in the ecosystem. My backpack is worth thousands of dollars and I know that I'm one vulnerability away from losing it all. A user can do everything right and still have their items stolen because of a zero day exploit in a program they use.

As an added bonus, because block chains are distributed databases, item ownership information becomes much more resilient. There's a [light client protocol][light] which allows applications to just watch the state of a specific contract, while still having some cryptographic assurance about the current state of the world. Users would be able to prove that they own items in game even when the centralized item servers go down.

From a security standpoint, _something_ like the system I'm outlining is needed to stop the rampant hacking, but this system has costs to everyone, and it is important to consider the trade-offs being made here.

### Downsides for Users

From the user standpoint, there's a loss of convenience. While the trade conformation emails Valve currently sends aren't exactly convenient, it does mean you can trade from anywhere you have a browser. With the system I'm proposing, you'd have to have a dedicated hardware dongle to sign transactions.

Likewise, the user is now on the hook for paying transaction fees to the Ethereum network. I personally am fine with paying a couple of cents per transaction, especially to protect my thousands of dollars of [Unusuals][], but this does mean that it will never make economic sense for the majority of free item drops, which are often worth less than a cent.

[Unusuals]: https://wiki.teamfortress.com/wiki/Unusual

Likewise, there's the cost of hardware. I assume that Valve could manufacture hardware much cheaper than any of the current Bitcoin hardware wallets. This would still be a cost for the users. It's one that I'd pay, and that I think many people would be willing to pay for, but it is still an up front cost.

Currently, when the item server isn't under pressure, operations on inventories complete fairly quickly. Transactions in blockchain based systems are only considered complete once a block has been generated that contains the transaction, and the target block time in Ethereum is 12 seconds. But as block minting is a probabilistic process, that's a target time and it can be significantly faster or slower. So while the system I'm outlining has better availability, it has poorer average and worse-case latency.

Finally, the user is on the hook for security of their encryption key. A user could fail to back their key up or could leak it to the internet. Both are catastrophic failure modes. One possible mitigation is to ship the security hardware with a the encryption key physically engraved onto fire resistant stainless steel, which would prevent losing it. There are many companies in the Bitcoin ecosystem which do this, such as [Cryobit][].

[Cryobit]: https://www.cryobit.co/

### Downsides for Valve

Given that it doesn't make economic sense for items worth under a penny to go on the blockchain, the current centralized item system probably has to stay. Interoperability becomes a consideration and would make any actual production ready system more complex.

Valve has a policy of retroactively modifying a player's items to be untradable if they're caught hacking, which would generally be circumvented if something like this was deployed. I suspect that in practice this wouldn't be much of a change. People using LMAOBOX Free (which Valve can detect) usually appear to be hacking with five minute old Steam accounts, which have no items and will probably last another ten to thirty minutes before being caught by [Valve Anti-Cheat][vac]. People hacking while wearing [Unusuals][] or wielding [Australium weapons][] are highly likely to be using the subscription LMAOBOX Premium, which Valve cannot detect. I suspect that this change would not much effect on the number of premium items that leave the economy due to being VACed.

[vac]: https://support.steampowered.com/kb_article.php?ref=7849-Radz-6869
[Australium weapons]: https://wiki.teamfortress.com/wiki/Australium_weapons

Finally, Valve currently doesn't gain any revenue from the high end Unusual market as their Steam Marketplace will only accept sell orders up to $400. (For reference, a [Golden Frying Pan][pan] usually goes for over $2000. A [Showstopper Conga][conga] goes for $800. And don't even _look_ at what [Burning Team Captains][teamcaptain] go for!) Trading these high value items on chain would be safer, without the chargeback risk that comes with PayPal. However, the Steam Marketplace does transact in lower value items, and Valve takes 15%. There are already 3rd party sellers of TF2 items who settle in fiat money, and this hasn't supplanted the official Marketplace. It's unlikely that any 3rd party marketplace built that interacts with the blockchain would take a large bite out of market profits, but it's still a risk that should be listed.

[pan]: http://backpack.tf/stats/Strange/Golden%20Frying%20Pan/Tradable/Craftable
[conga]: http://backpack.tf/stats/Unusual/Taunt%3A%20Conga/Tradable/Craftable/3001
[teamcaptain]: http://backpack.tf/stats/Unusual/Team%20Captain/Tradable/Craftable/13


[android]: http://androidvulnerabilities.org/
[cssrc]: https://www.reddit.com/r/GlobalOffensive/comments/3jpyhh/do_not_join_unkown_cs_source_servers_via_ip/
[TeamSpeak]: http://forum.teamspeak.com/showthread.php/120755-SECURITY-UPDATE-TeamSpeak-3-Client-3-0-18-1-is-Available
[trezor]: https://www.bitcointrezor.com/
[light]: https://github.com/ethereum/wiki/wiki/Light-client-protocol
