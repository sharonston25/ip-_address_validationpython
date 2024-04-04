import re

def validate_ip(ip):

    ip_regex = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    if re.match(ip_regex, ip):
        return True
    else:
        return False



def print_binary(ip):
    
    octets = ip.split('.')
    
    
    for octet in octets:
        binary_octet = bin(int(octet))[2:].zfill(8)
        print(binary_octet, end=' ')
    print()

def main():
   
    ip = input("Enter IP address: ")
    if validate_ip(ip):
         print("valid");
    
    
  
    if not validate_ip(ip):
        print_binary(ip)
        print("Invalid IP address")
    
    
        return 1
    
    
    print("Binary representation of IP address:")
    print_binary(ip)
    
  
    

if __name__ == "__main__":
    result = main()
    exit(result)