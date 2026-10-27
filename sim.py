import random

def generateRandomIP():
    return f"173.91.204.{random.randint(15,50)}"

def checkFirewallRules(ip, rules):
    for ruleIP, action in rules.items():
        if ip == ruleIP:
            return action
    return "allow"

def main():
    firewallRules = {
        "173.91.204.17" : "block",
        "173.91.204.23" : "block",
        "173.91.204.26" : "block",
        "173.91.204.34" : "block",
        "173.91.204.42" : "block",
        "173.91.204.48" : "block"
    }

    for x in range(12):
        ipAddress = generateRandomIP()
        action = checkFirewallRules(ipAddress, firewallRules)
        randomNum = random.randint(0,9999)
        print(f"IP: {ipAddress}, Action: {action}, Random: {randomNum}")


if __name__ == "__main__":
    main()