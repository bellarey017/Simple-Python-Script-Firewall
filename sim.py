import random

""" This first function generates source IP addresses, 
representing inbound connections from randomly selected IP addresses. """

def generateRandomIP():
    return f"173.91.204.{random.randint(15,50)}"

"""By predefining firewall rules, the script then evaluates the IP address
against said rules. This simulates the decision making of a basic firewall. """

def checkFirewallRules(ip, rules):
    for ruleIP, action in rules.items():
        if ip == ruleIP:
            return action
    return "allow" # Policy made to allow traffic to come through.



def main():

    # Defining a list of blocked IP addresses, representing malicious hosts.
    firewallRules = {
        "173.91.204.17" : "block",
        "173.91.204.23" : "block",
        "173.91.204.26" : "block",
        "173.91.204.34" : "block",
        "173.91.204.42" : "block",
        "173.91.204.48" : "block"
    }

    """ Incoming traffic, each iteration represents a new connection 
    attempt being evaluated by the firewall. """
    
    for x in range(12):
        ipAddress = generateRandomIP()
        action = checkFirewallRules(ipAddress, firewallRules) # Determine traffic acceptance based on rules.
        randomNum = random.randint(0,9999) # Simulation of connection identifiers.
        print(f"IP: {ipAddress}, Action: {action}, Random: {randomNum}") # Log output.


# Program entry point.
if __name__ == "__main__":
    main()
