#BeaglebonePython bone.py API for interfacing to the hardware of the Beagleboard's Beaglebone platform
#running the stock Angstrom Linux distribution. 
import os

######################################################################
# Title:  General Purpose Input and Output Constants and Functions   #
# Edited/Revised: Bryan on 29 August 2012                            #
# Version: 1.0                                                       #
######################################################################
#Beaglebone Pin Definitions --- links to the definitions below, structure taken from bone.js
#PORT 8 Definitions
P8_2 = "P8_2"	# GND
P8_3 = "P8_3"	# GPIO1_6
P8_4 = "P8_4"	# GPIO1_7
P8_5 = "P8_5"	# GPIO1_2
P8_6 = "P8_6"	# GPIO1_3
P8_7 = "P8_7"	# TIMER 4
P8_8 = "P8_8"	# TIMER 7
P8_9 = "P8_9"	# TIMER 5
P8_10 = "P8_10"	# TIMER 6
P8_11 = "P8_11"	# GPIO1_13
P8_12 = "P8_12"	# GPIO1_12
P8_13 = "P8_13"	# EHRPWM 2B
P8_14 = "P8_14"	# GPIO0_26
P8_15 = "P8_15"	# GPIO1_15
P8_16 = "P8_16"	# GPIO1_14
P8_17 = "P8_17"	# GPIO0_27
P8_18 = "P8_18"	# GPIO2_1
P8_19 = "P8_19"	# EHRPWM 2A
P8_20 = "P8_20"	# GPIO1_31
P8_21 = "P8_21"	# GPIO1_30
P8_22 = "P8_22"	# GPIO1_5
P8_23 = "P8_23"	# GPIO1_4
P8_24 = "P8_24"	# GPIO1_1
P8_25 = "P8_25"	# GPIO1_0
P8_26 = "P8_26"	# GPIO1_29
P8_27 = "P8_27"	# GPIO2_22
P8_28 = "P8_28"	# GPIO2_24
P8_29 = "P8_29"	# GPIO2_23
P8_30 = "P8_30"	# GPIO2_25
P8_31 = "P8_31"	# UART5_CTSN
P8_32 = "P8_32"	# UART5_RTSN
P8_33 = "P8_33"	# UART4_RTSN
P8_34 = "P8_34"	# UART3_RTSN
P8_35 = "P8_35"	# UART4_CTSN
P8_36 = "P8_36"	# UART3_CTSN
P8_37 = "P8_37"	# UART5_TXD
P8_38 = "P8_38"	# UART5_RXD
P8_39 = "P8_39"	# GPIO2_12
P8_40 = "P8_40"	# GPIO2_13
P8_41 = "P8_41"	# GPIO2_10
P8_42 = "P8_42"	# GPIO2_11
P8_43 = "P8_43"	# GPIO2_8
P8_44 = "P8_44"	# GPIO2_9
P8_45 = "P8_45"	# GPIO2_6
P8_46 = "P8_46"	# GPIO2_7

#PORT 9 Definitions
P9_1 = "P9_1"	# GND
P9_2 = "P9_2"	# GND
P9_3 = "P9_3"	# Vdd 3V3 EXP
P9_4 = "P9_4"	# Vdd 3V3 EXP
P9_5 = "P9_5"	# Vdd 5V
P9_6 = "P9_6"	# Vdd 5V
P9_7 = "P9_7"	# SYS 5V
P9_8 = "P9_8"	# SYS 5V
P9_9 = "P9_9"	# PWR BUTTON
P9_10 = "P9_10"	# SYS RESET
P9_11 = "P9_11"	# UART4_RXD
P9_12 = "P9_12"	# GPIO1_28
P9_13 = "P9_13"	# UART4_TXD
P9_14 = "P9_14"	# EHRPWM 1A
P9_15 = "P9_15"	# GPIO1_16
P9_16 = "P9_16"	# EHRPWM 1B
P9_17 = "P9_17"	# I2C1_SCL
P9_18 = "P9_18"	# I2C1_SDA
P9_19 = "P9_19"	# I2C2_SCL
P9_20 = "P9_20"	# I2C2_SDA
P9_21 = "P9_21"	# UART2_TXD
P9_22 = "P9_22"	# UART2_RXD
P9_23 = "P9_23"	# GPIO1_17
P9_24 = "P9_24"	# UART1_TXD
P9_25 = "P9_25"	# GPIO3_21
P9_26 = "P9_26"	# UART1_RXD
P9_27 = "P9_27"	# GPIO3_19
P9_28 = "P9_28"	# SPI1_CS0
P9_29 = "P9_29"	# SPI1_DO
P9_30 = "P9_30"	# SPI1_DI
P9_31 = "P9_31"	# SPI1_SCK
P9_32 = "P9_32"	# Vdd ADC (1.8V)
P9_33 = "P9_33"	# AIN 4
P9_34 = "P9_34"	# ADC GND
P9_35 = "P9_35"	# AIN 6
P9_36 = "P9_36"	# AIN 5
P9_37 = "P9_37"	# AIN 2
P9_38 = "P9_38"	# AIN 3
P9_39 = "P9_39"	# AIN 0
P9_40 = "P9_40"	# AIN 1
P9_41 = "P9_41"	# CLKOUT 2
P9_42 = "P9_42"	# GPIO0_7
P9_43 = "P9_43"	# GND
P9_44 = "P9_44"	# GND
P9_45 = "P9_45"	# GND
P9_46 = "P9_46"	# GND

# -------------- from bonescript's bone.js ----------------------
gpio0 = 0
gpio1 = gpio0+32
gpio2 = gpio1+32
gpio3 = gpio2+32

bone = { "P8_1": { "name": "DGND" },
	"P8_2": { "name": "DGND" },
	"P8_3": { "name": "GPIO1_6", "gpio": gpio1+6, "mux": "gpmc_ad6", "eeprom": 26 },
	"P8_4": { "name": "GPIO1_7", "gpio": gpio1+7, "mux": "gpmc_ad7", "eeprom": 27 },
	"P8_5": { "name": "GPIO1_2", "gpio": gpio1+2, "mux": "gpmc_ad2", "eeprom": 22 },
	"P8_6": { "name": "GPIO1_3", "gpio": gpio1+3, "mux": "gpmc_ad3", "eeprom": 23 },
	"P8_7": { "name": "TIMER4", "gpio": gpio2+2, "mux": "gpmc_advn_ale", "eeprom": 41 },
	"P8_8": { "name": "TIMER7", "gpio": gpio2+3, "mux": "gpmc_oen_ren", "eeprom": 44 },
	"P8_9": { "name": "TIMER5", "gpio": gpio2+5, "mux": "gpmc_ben0_cle", "eeprom": 42 },
	"P8_10": { "name": "TIMER6", "gpio": gpio2+4, "mux": "gpmc_wen", "eeprom": 43 },
	"P8_11": { "name": "GPIO1_13", "gpio": gpio1+13, "mux": "gpmc_ad13", "eeprom": 29 },
	"P8_12": { "name": "GPIO1_12", "gpio": gpio1+12, "mux": "gpmc_ad12", "eeprom": 28 },
	"P8_13": { "name": "EHRPWM2B", "gpio": gpio0+23, "mux": "gpmc_ad9", "eeprom": 15 },
	"P8_14": { "name": "GPIO0_26", "gpio": gpio0+26, "mux": "gpmc_ad10", "eeprom": 16 },
	"P8_15": { "name": "GPIO1_15", "gpio": gpio1+15, "mux": "gpmc_ad15", "eeprom": 31 },
	"P8_16": { "name": "GPIO1_14", "gpio": gpio1+14, "mux": "gpmc_ad14", "eeprom": 30 },
	"P8_17": { "name": "GPIO0_27", "gpio": gpio0+27, "mux": "gpmc_ad11", "eeprom": 17 },
	"P8_18": { "name": "GPIO2_1", "gpio": gpio2+1, "mux": "gpmc_clk", "eeprom": 40 },
	"P8_19": { "name": "EHRPWM2A", "gpio": gpio0+22, "mux": "gpmc_ad8", "eeprom": 14 },
	"P8_20": { "name": "GPIO1_31", "gpio": gpio1+31, "mux": "gpmc_csn2", "eeprom": 39 },
	"P8_21": { "name": "GPIO1_30", "gpio": gpio1+30, "mux": "gpmc_csn1", "eeprom": 38 },
	"P8_22": { "name": "GPIO1_5", "gpio": gpio1+5, "mux": "gpmc_ad5", "eeprom": 25 },
	"P8_23": { "name": "GPIO1_4", "gpio": gpio1+4, "mux": "gpmc_ad4", "eeprom": 24 },
	"P8_24": { "name": "GPIO1_1", "gpio": gpio1+1, "mux": "gpmc_ad1", "eeprom": 21 },
	"P8_25": { "name": "GPIO1_0", "gpio": gpio1+0, "mux": "gpmc_ad0", "eeprom": 20 },
	"P8_26": { "name": "GPIO1_29", "gpio": gpio1+29, "mux": "gpmc_csn0", "eeprom": 37 },
	"P8_27": { "name": "GPIO2_22", "gpio": gpio2+22, "mux": "lcd_vsync", "eeprom": 57 },
	"P8_28": { "name": "GPIO2_24", "gpio": gpio2+24, "mux": "lcd_pclk", "eeprom": 59 },
	"P8_29": { "name": "GPIO2_23", "gpio": gpio2+23, "mux": "lcd_hsync", "eeprom": 58 },
	"P8_30": { "name": "GPIO2_25", "gpio": gpio2+25, "mux": "lcd_ac_bias_en", "eeprom": 60 },
	"P8_31": { "name": "UART5_CTSN", "gpio": gpio0+10, "mux": "lcd_data14", "eeprom": 7 },
	"P8_32": { "name": "UART5_RTSN", "gpio": gpio0+11, "mux": "lcd_data15", "eeprom": 8 },
	"P8_33": { "name": "UART4_RTSN", "gpio": gpio0+9, "mux": "lcd_data13", "eeprom": 6 },
	"P8_34": { "name": "UART3_RTSN", "gpio": gpio2+17, "mux": "lcd_data11", "eeprom": 56 },
	"P8_35": { "name": "UART4_CTSN", "gpio": gpio0+8, "mux": "lcd_data12", "eeprom": 5 },
	"P8_36": { "name": "UART3_CTSN", "gpio": gpio2+16, "mux": "lcd_data10", "eeprom": 55 },
	"P8_37": { "name": "UART5_TXD", "gpio": gpio2+14, "mux": "lcd_data8", "eeprom": 53 },
	"P8_38": { "name": "UART5_RXD", "gpio": gpio2+15, "mux": "lcd_data9", "eeprom": 54 },
	"P8_39": { "name": "GPIO2_12", "gpio": gpio2+12, "mux": "lcd_data6", "eeprom": 51 },
	"P8_40": { "name": "GPIO2_13", "gpio": gpio2+13, "mux": "lcd_data7", "eeprom": 52 },
	"P8_41": { "name": "GPIO2_10", "gpio": gpio2+10, "mux": "lcd_data4", "eeprom": 49 },
	"P8_42": { "name": "GPIO2_11", "gpio": gpio2+11, "mux": "lcd_data5", "eeprom": 50 },
	"P8_43": { "name": "GPIO2_8", "gpio": gpio2+8, "mux": "lcd_data2", "eeprom": 47 },
	"P8_44": { "name": "GPIO2_9", "gpio": gpio2+9, "mux": "lcd_data3", "eeprom": 48 },
	"P8_45": { "name": "GPIO2_6", "gpio": gpio2+6, "mux": "lcd_data0", "eeprom": 45 },
	"P8_46": { "name": "GPIO2_7", "gpio": gpio2+7, "mux": "lcd_data1", "eeprom": 46 },
	"P9_1": { "name": "DGND" },
	"P9_2": { "name": "DGND" },
	"P9_3": { "name": "VDD_3V3" },
	"P9_4": { "name": "VDD_3V3" },
	"P9_5": { "name": "VDD_5V" },
	"P9_6": { "name": "VDD_5V" },
	"P9_7": { "name": "SYS_5V" },
	"P9_8": { "name": "SYS_5V" },
	"P9_9": { "name": "PWR_BUT" },
	"P9_10": { "name": "SYS_RESETn" },
	"P9_11": { "name": "UART4_RXD", "gpio": gpio0+30, "mux": "gpmc_wait0", "eeprom": 18 },
	"P9_12": { "name": "GPIO1_28", "gpio": gpio1+28, "mux": "gpmc_ben1", "eeprom": 36 },
	"P9_13": { "name": "UART4_TXD", "gpio": gpio0+31, "mux": "gpmc_wpn", "eeprom": 19 },
	"P9_14": { "name": "EHRPWM1A", "gpio": gpio1+18, "mux": "gpmc_a2", "eeprom": 34, "pwm" : "ehrpwm.1:0" },
	# NOTE - following was set to mux name mii1_rxd3, which caused hang!
	"P9_15": { "name": "GPIO1_16", "gpio": gpio1+16, "mux": "gpmc_a0", "eeprom": 32 },
	"P9_16": { "name": "EHRPWM1B", "gpio": gpio1+19, "mux": "gpmc_a3", "eeprom": 35, "pwm" : "ehrpwm.1:1" },
	"P9_17": { "name": "I2C1_SCL", "gpio": gpio0+5, "mux": "spi0_cs0", "eeprom": 3 },
	"P9_18": { "name": "I2C1_SDA", "gpio": gpio0+4, "mux": "spi0_d1", "eeprom": 2 },
	"P9_19": { "name": "I2C2_SCL", "gpio": gpio0+13, "mux": "uart1_rtsn", "eeprom": 9 },
	"P9_20": { "name": "I2C2_SDA", "gpio": gpio0+12, "mux": "uart1_ctsn", "eeprom": 10 },
	"P9_21": { "name": "UART2_TXD", "gpio": gpio0+3, "mux": "spi0_d0", "eeprom": 1 },
	"P9_22": { "name": "UART2_RXD", "gpio": gpio0+2, "mux": "spi0_sclk", "eeprom": 0 },
	"P9_23": { "name": "GPIO1_17", "gpio": gpio1+17, "mux": "gpmc_a1", "eeprom": 33 },
	"P9_24": { "name": "UART1_TXD", "gpio": gpio0+15, "mux": "uart1_txd", "eeprom": 12 },
	"P9_25": { "name": "GPIO3_21", "gpio": gpio3+21, "mux": "mcasp0_ahclkx", "eeprom": 66 },
	"P9_26": { "name": "UART1_RXD", "gpio": gpio0+14, "mux": "uart1_rxd", "eeprom": 11 },
	"P9_27": { "name": "GPIO3_19", "gpio": gpio3+19, "mux": "mcasp0_fsr", "eeprom": 64 },
	"P9_28": { "name": "SPI1_CS0", "gpio": gpio3+17, "mux": "mcasp0_ahclkr", "eeprom": 63 },
	"P9_29": { "name": "SPI1_D0", "gpio": gpio3+15, "mux": "mcasp0_fsx", "eeprom": 61 },
	"P9_30": { "name": "SPI1_D1", "gpio": gpio3+16, "mux": "mcasp0_axr0", "eeprom": 62 },
	"P9_31": { "name": "SPI1_SCLK", "gpio": gpio3+14, "mux": "mcasp0_aclkx", "eeprom": 65 },
	"P9_32": { "name": "VDD_ADC" },
	"P9_33": { "name": "AIN4", "eeprom": 71 },
	"P9_34": { "name": "GNDA_ADC" },
	"P9_35": { "name": "AIN6", "eeprom": 73 },
	"P9_36": { "name": "AIN5", "eeprom": 72 },
	"P9_37": { "name": "AIN2", "eeprom": 69 },
	"P9_38": { "name": "AIN3", "eeprom": 70 },
	"P9_39": { "name": "AIN0", "eeprom": 67 },
	"P9_40": { "name": "AIN1", "eeprom": 68 },
	"P9_41": { "name": "CLKOUT2", "gpio": gpio0+20, "mux": "xdma_event_intr1", "eeprom": 13 },
	"P9_42": { "name": "GPIO0_7", "gpio": gpio0+7, "mux": "ecap0_in_pwm0_out", "eeprom": 4 },
	"P9_43": { "name": "DGND" },
	"P9_44": { "name": "DGND" },
	"P9_45": { "name": "DGND" },
	"P9_46": { "name": "DGND" },
}

######################################################################
# Title:  GPIO Constants and Functions                               #
# Edited/Revised: August 18, 2012 by Bryan                           #
# Version: 1.0                                                       #
######################################################################
GPIO_DIR = "/sys/class/gpio"
OMAP_MUX_DIR = "/sys/kernel/debug/omap_mux"
HIGH = "1"
LOW = "0"
INPUT = "in"
OUTPUT = "out"

#Set the pin mode to either an output or an input (MODE 7)
def SetPinMode(pin, mode):
	pinNumber = str(bone[pin]["gpio"])
	print "pinNumber="+pinNumber

	if mode == "in":
		open(OMAP_MUX_DIR + "/"+ bone[pin]["mux"], 'w').write("27")
	else:
		open(OMAP_MUX_DIR + "/"+ bone[pin]["mux"], 'w').write("7")
		
	if not os.path.exists(GPIO_DIR + "/gpio" + pinNumber):
		open(GPIO_DIR + "/export", 'w').write(pinNumber)		
	
	if mode in (INPUT, OUTPUT):
		open(GPIO_DIR + "/gpio"+pinNumber+"/direction", 'w').write(mode)

# Set pins to be active loe, they will report a 1 to linux if the input is low
# This is common for interrupt-based systems instead of being active high.
def SetPinsActiveLow(value):
	if value:
		open(GPIO_DIR + "/active_low", 'w').write("1")
	else:
		open(GPIO_DIR + "/active_low", 'w').write("0")
		
#Unexport and free the pin for future use by other programs
def FreePin(pin):
	pinNumber = str(bone[pin]["gpio"])
	if os.path.exists(GPIO_DIR + "/gpio" + pinNumber):
		open(GPIO_DIR + "/unexport", 'w').write(pinNumber)

#Write to the pin either a 1 (Vcc=3.3V) or a 0 (Gnd)
def DigitalWrite(pin, value):
	pinNumber = str(bone[pin]["gpio"])
	if os.path.exists(GPIO_DIR + "/gpio" + pinNumber):
		if value in (HIGH, LOW):
			open(GPIO_DIR + "/gpio"+pinNumber+"/value", 'w').write(value)

#If the pin is set up to be an input, read from it			
def DigitalRead(pin):
	pinNumber = str(bone[pin]["gpio"])
	if os.path.exists(GPIO_DIR + "/gpio" + pinNumber):
			return open(GPIO_DIR + "/gpio"+pinNumber+"/value", 'r').read()

#User LEDs add into GPIO class
#USER0 and USER1 are controlled by Angstron - SD read/write and the heartbeat LED
# USER2 and USER3 are, in fact, user controllable for programming
# Turn the LED On - Pass in USER0 to USER3 LEDs on the main board

LED_DIR = "/sys/devices/platform/leds-gpio/leds/"
USR0 = '0'
USR1 = '1'
USR2 = '2'
USR3 = '3'

def led_on(led):
	open(LED_DIR+"beaglebone::usr"+led+"/brightness", 'w').write('1')

# Turn the LED Off - pass in USER0 to USER3 LEDs on the main board
def led_off(led):
	open(LED_DIR+"beaglebone::usr"+led+"/brightness", 'w').write('0')

# Toggle the USER LED - pass in USESR0 to USER3 on the main board
def led_toggle(led):
	if open(LED_DIR+"beaglebone::usr"+led+"/brightness", 'w').read() == '0':
		open(LED_DIR+"beaglebone::usr"+led+"/brightness", 'w').write('1')
	else:
		open(LED_DIR+"beaglebone::usr"+led+"/brightness", 'w').write('0')
				
######################################################################
# Title:  UART Serial Read/Write Constants and Functions             #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...	
#class uart:
	#definitions
	
######################################################################
# Title:  Analog Input Constants and Functions                       #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...
#class adc:
	#definitions

######################################################################
# Title:  Analog Output/Pulse Width Mod. Constants and Functions     #
# Edited/Revised:                                                    #
# Version: 1.0                                                       #
######################################################################

# More to come here...
#class pwm:
	#definitions

######################################################################
# Title:  RC Servo Output Constants and Functions                    #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...
#class servo:
	#definitions

######################################################################
# Title:  One Wire Read (DS18B20) Constants and Functions            #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...
#class onewire:
	#definitions

######################################################################
# Title:  I2C Read/Write Constants and Functions                     #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...
#class i2c:
	#definitions

######################################################################
# Title:  SPI Read/Write Constants and Functions                     #
# Edited/Revised:                                                    #
# Version: 0.0                                                       #
######################################################################

# More to come here...
#class spi:
	#definitions
	
