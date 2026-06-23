# ==============================================================================
# INDUSTRIAL COMMUNICATIONS LOG: TRACK Python PROGRAMMING PROJECT
# REPOSITORY REGISTER OWNER : Swetha_OIBSIP
# DATA TRANSMISSION LAYER   : SOCKET LOOPBACK CORE NETWORK (NO EXTERNAL PIP)
# ==============================================================================

import socket
import sys

# Custom workspace identification keys
NETWORK_NODE_ID = "Swetha_OIBSIP_NODE_A"

def launch_networking_terminal():
    # Premium Engineering Banner Layout for Project Submission
    print("\n" + "#" * 65)
    print("##  DATA LAYER SUITE: LOOPBACK NETWORK CHAT CONFIGURATION       ##")
    print(f"##  DEVELOPER ACCESS TIER : {NETWORK_NODE_ID}                  ##")
    print("##  INFRASTRUCTURE STATUS : SOCKET ROUTING BUFFER READY         ##")
    print("#" * 65)

    print("\nSelect Operational Mode Configuration:")
    print(" 1. Deploy System Network Server Panel")
    print(" 2. Connect Client Station Node to Network")
    
    user_selection = input("\nSelect Execution Layer (1 or 2): ").strip()

    # Define common loopback parameters to ensure offline reliability inside Pydroid
    IP_LOOPBACK = "127.0.0.1"
    PORT_ASSIGNED = 9999

    # ==========================================================================
    # MODE 1: NETWORK SERVER ROUTING ARCHITECTURE
    # ==========================================================================
    if user_selection == "1":
        print(f"\n📡 Instantiating Server Protocol Engine on host local matrix...")
        
        # Initialize internal communication stream socket mapping
        server_socket_bus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Bind and configure queue buffers
            server_socket_bus.bind((IP_LOOPBACK, PORT_ASSIGNED))
            server_socket_bus.listen(1)
            print(f"✅ Host active! Server listening on loopback endpoint [{IP_LOOPBACK}:{PORT_ASSIGNED}]")
            print("⏳ Awaiting external node communication sequence request...")
            
            client_connection, remote_address = server_socket_bus.accept()
            print(f"\n🤝 Secure link established with remote address profile: {remote_address}")
            
            # Interactive Data Exchange Loop
            while True:
                # Intercept incoming encrypted/raw byte packages
                payload_captured = client_connection.recv(1024).decode('utf-8')
                if not payload_captured or payload_captured.lower() == 'disconnect':
                    print("\n⚠️ Connection terminate signal received. Dropping stream proxy.")
                    break
                    
                print(f"\n📥 [INCOMING MESSAGE] Client Node: {payload_captured}")
                
                # Outbound message construction
                reply_string = input("📤 [OUTBOUND REPLY] Type Server Message (or 'disconnect'): ").strip()
                client_connection.send(reply_string.encode('utf-8'))
                
                if reply_string.lower() == 'disconnect':
                    break
                    
            client_connection.close()
            
        except Exception as system_fault:
            print(f"❌ Structural Socket Fault Encountered: {system_fault}")
        finally:
            server_socket_bus.close()
            print("\n🏁 Server operational routine terminated safely.")

    # ==========================================================================
    # MODE 2: REMOTE CLIENT CONNECTOR NODE
    # ==========================================================================
    elif user_selection == "2":
        print(f"\n🛰️ Triggering Client Station Connector Sequence...")
        
        client_socket_bus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            print(f"Connecting to centralized terminal loopback host architecture [{IP_LOOPBACK}:{PORT_ASSIGNED}]...")
            client_socket_bus.connect((IP_LOOPBACK, PORT_ASSIGNED))
            print("✅ Handshake confirmation verified! Connection pipeline open.")
            print("Type data packets below. Set command string to 'disconnect' to exit session.")
            
            while True:
                outbound_packet = input("\n📝 [MESSAGE BUFFER] Enter text package: ").strip()
                if not outbound_packet:
                    continue
                    
                # Transmit structured raw data packets across socket pipe
                client_socket_bus.send(outbound_packet.encode('utf-8'))
                
                if outbound_packet.lower() == 'disconnect':
                    print("⚠️ Transmission stopped. Terminating station interface connection.")
                    break
                
                # Intercept dynamic server response confirmation packet
                print("⏳ Synchronizing server feedback buffer...")
                server_response_packet = client_socket_bus.recv(1024).decode('utf-8')
                print(f"📥 [SERVER RESPONSE] Host Matrix: {server_response_packet}")
                
                if server_response_packet.lower() == 'disconnect':
                    print("\n⚠️ Host disconnected remote channel layer.")
                    break
                    
        except ConnectionRefusedError:
            print("\n❌ Gateway Error: Connection refused by target terminal.")
            print("💡 Pro-Tip: Run Mode 1 (Server) first in a separate terminal before choosing Mode 2!")
        except Exception as system_fault:
            print(f"❌ Network Bus Fault: {system_fault}")
        finally:
            client_socket_bus.close()
            print("\n🏁 Client terminal workspace session closed.")
            
    else:
        print("⚠️ Entry sequence unmapped. Select option 1 or 2.")

if __name__ == "__main__":
    launch_networking_terminal()
