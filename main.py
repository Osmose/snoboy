from snoboy import memory, cart, cpu, instructions

def main():
	cart.loadCart('sml.gb')

	for i in range(0,25):
		cpu.doInstruction()

if __name__ == "__main__":
	main()