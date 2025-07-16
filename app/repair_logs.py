repair_logs = [
    "Customer reports frequent battery overheating warnings during fast charging sessions above 100 kW. Issue occurs in warm weather conditions (~35°C). Affects 2022 Audi Q4 e-tron, VIN: WA1VABFZ6NP012345. Technician noticed fan speed remains low during charging. Firmware version: BMS_4.2.1.",
    "The vehicle intermittently loses regenerative braking functionality during downhill driving. Affects 2021 BMW iX3, VIN: WBXEVF12345678901. Technician observed error code RB-32 in the brake control module. Software version: BRK_SW_3.7.0.",
    "Driver complains of inconsistent climate control performance, especially sudden drops in cabin temperature during high humidity. Affects 2023 Mercedes EQC, VIN: WDC0X4EB6PF123456. Diagnostics reveal intermittent sensor failure on the HVAC module. Firmware version: HVAC_2.0.5.",
    "The infotainment system freezes when connecting certain Android smartphones via USB. Reported in 2022 Volkswagen ID.4, VIN: WVWKR7AU6NW123456. Technician found outdated firmware on the MIB2 system. Firmware version: MIB2_7.5.3.",
    "Frequent alerts about low tire pressure despite normal PSI readings on all tires. Occurs in 2021 Porsche Taycan, VIN: WP0AA2Y10MS123456. Technician suspects faulty TPMS sensor on front left wheel. Software version: TPMS_1.1.9."
]

with open("repair_logs_sample.txt", "w") as f:
    for log in repair_logs:
        f.write(log + "\n\n")

print("Sample repair logs saved to repair_logs_sample.txt")

