import re

# Example of usage:
md_tables = [
    """
| Roll | Injury Description                                  | Recovery Time   | Scars               |
|------|-----------------------------------------------------|-----------------|---------------------|
| 1    | Light head bump, minor discomfort                   | 1d4 hours       | N/A                 |
| 2    | Forehead knock, slight headache                     | 1d4 hours       | N/A                 |
| 3    | Ear hit, temporary ringing and pain                 | 1d4 hours       | N/A                 |
| 4    | Nose impact, minor bleeding and discomfort          | 1d4 hours       | N/A                 |
| 5    | Crown hit, momentary dizziness                      | 1d4 hours       | N/A                 |
| 6    | Cheek strike, slight swelling                       | 1d4 hours       | N/A                 |
| 7    | Chin impact, stinging pain                          | 1d4 hours       | N/A                 |
| 8    | Temple bump, moderate headache                      | 1d4 hours       | N/A                 |
| 9    | Face slam, disoriented and headache                 | 1d4 hours       | N/A                 |
| 10   | Eye socket hit, risk of vision issues               | 1d4 days        | N/A                 |
| 11   | Skull jolt, potential for migraines                 | 1d4 days        | N/A                 |
| 12   | Facial fracture, severe pain                        | 1d4 weeks       | N/A                 |
| 13   | Head impact, risk of concussion                     | 1d4 weeks       | N/A                 |
| 14   | Severe brain trauma, unconsciousness                | 1d4 weeks       | N/A                 |
| 15   | Critical hit, cranial collapse                      | Instant death   | N/A                 |
| 16   | Critical hit, brain rupture                         | Instant death   | N/A                 |
| 17   | Critical hit, instant brain death                   | Instant death   | N/A                 |
| 18   | Critical hit, skull shattered                       | Instant death   | N/A                 |
| 19   | Critical hit, massive internal bleeding             | Instant death   | N/A                 |
| 20   | Critical hit, head explosion                        | Instant death   | N/A                 |
    """,
    """
| Roll | Injury Description                         | Recovery Time | Scars |
|------|--------------------------------------------|---------------|-------|
| 1    | Bruised ribs, mild discomfort              | 1d4 hours     | N/A   |
| 2    | Solar plexus hit, shortness of breath      | 1d4 hours     | N/A   |
| 3    | Abdominal punch, temporary nausea          | 1d4 hours     | N/A   |
| 4    | Lower rib impact, minor pain               | 1d4 hours     | N/A   |
| 5    | Sides struck, momentary weakness           | 1d4 hours     | N/A   |
| 6    | Upper abdomen blow, slight swelling        | 1d4 hours     | N/A   |
| 7    | Diaphragm hit, difficulty breathing        | 1d4 hours     | N/A   |
| 8    | Sternum impact, moderate discomfort        | 1d4 hours     | N/A   |
| 9    | Rib cage shock, disorientation             | 1d4 hours     | N/A   |
| 10   | Organ bruise, potential complications      | 1d4 days      | N/A   |
| 11   | Internal bleeding, risk of infection       | 1d4 days      | N/A   |
| 12   | Rib fracture, severe pain                  | 1d4 weeks     | N/A   |
| 13   | Spleen or liver damage, risk of shock      | 1d4 weeks     | N/A   |
| 14   | Critical hit, vital organ rupture          | Instant death | N/A   |
| 15   | Critical hit, cardiac arrest               | Instant death | N/A   |
| 16   | Critical hit, internal organs obliterated  | Instant death | N/A   |
| 17   | Critical hit, massive hemorrhage           | Instant death | N/A   |
| 18   | Critical hit, torso shattered              | Instant death | N/A   |
| 19   | Critical hit, torso explosion              | Instant death | N/A   |
| 20   | Critical hit, instant torso disintegration | Instant death | N/A   |
    """,
    """
| Roll | Injury Description                           | Recovery Time   | Scars |
|------|----------------------------------------------|-----------------|-------|
| 1    | Minor bruising, mild discomfort              | 1d4 hours       | N/A   |
| 2    | Elbow knock, slight soreness                 | 1d4 hours       | N/A   |
| 3    | Forearm hit, temporary weakness              | 1d4 hours       | N/A   |
| 4    | Wrist impact, minor pain and stiffness       | 1d4 hours       | N/A   |
| 5    | Hand struck, momentary numbness              | 1d4 hours       | N/A   |
| 6    | Fingers jammed, slight swelling              | 1d4 hours       | N/A   |
| 7    | Shoulder impact, stinging pain               | 1d4 hours       | N/A   |
| 8    | Upper arm blow, moderate discomfort          | 1d4 hours       | N/A   |
| 9    | Dislocated joint, risk of complications      | 1d4 days        | N/A   |
| 10   | Fractured bone, potential for deformity      | 1d4 days        | N/A   |
| 11   | Severely dislocated joint, loss of function  | 1d4 weeks       | N/A   |
| 12   | Arm bone shattered, severe pain              | 1d4 weeks       | N/A   |
| 13   | Critical hit, arm amputation                 | Instant death   | N/A   |
| 14   | Critical hit, shattered arm                  | Instant death   | N/A   |
| 15   | Critical hit, arm obliteration               | Instant death   | N/A   |
| 16   | Critical hit, arm torn off                   | Instant death   | N/A   |
| 17   | Critical hit, massive arm hemorrhage         | Instant death   | N/A   |
| 18   | Critical hit, arm explosion                  | Instant death   | N/A   |
| 19   | Critical hit, instant arm disintegration     | Instant death   | N/A   |
| 20   | Critical hit, arm vaporization               | Instant death   | N/A   |
    """,
    """
| Roll | Injury Description                            | Recovery Time   | Scars |
|------|-----------------------------------------------|-----------------|-------|
| 1    | Minor shin bump, slight discomfort            | 1d4 hours       | N/A   |
| 2    | Knee hit, temporary limping                   | 1d4 hours       | N/A   |
| 3    | Thigh impact, momentary weakness              | 1d4 hours       | N/A   |
| 4    | Calf struck, minor pain and stiffness         | 1d4 hours       | N/A   |
| 5    | Ankle twisted, brief numbness                 | 1d4 hours       | N/A   |
| 6    | Foot stepped on, slight swelling              | 1d4 hours       | N/A   |
| 7    | Groin impact, stinging pain                   | 1d4 hours       | N/A   |
| 8    | Upper leg blow, moderate discomfort           | 1d4 hours       | N/A   |
| 9    | Dislocated joint, risk of complications       | 1d4 days        | N/A   |
| 10   | Fractured bone, potential for deformity       | 1d4 days        | N/A   |
| 11   | Severely dislocated joint, loss of function   | 1d4 weeks       | N/A   |
| 12   | Leg bone shattered, severe pain               | 1d4 weeks       | N/A   |
| 13   | Critical hit, leg amputation                  | Instant death   | N/A   |
| 14   | Critical hit, shattered leg                   | Instant death   | N/A   |
| 15   | Critical hit, leg obliteration                | Instant death   | N/A   |
| 16   | Critical hit, leg torn off                    | Instant death   | N/A   |
| 17   | Critical hit, massive leg hemorrhage          | Instant death   | N/A   |
| 18   | Critical hit, leg explosion                   | Instant death   | N/A   |
| 19   | Critical hit, instant leg disintegration      | Instant death   | N/A   |
| 20   | Critical hit, leg vaporization                | Instant death   | N/A   |
    """,
    """
| Roll | Injury Description                                  | Recovery Time   | Scars |
|------|-----------------------------------------------------|-----------------|-------|
| 1    | Minor abdomen bump, slight discomfort               | 1d4 hours       | N/A   |
| 2    | Belly hit, brief nausea                             | 1d4 hours       | N/A   |
| 3    | Midriff impact, momentary weakness                  | 1d4 hours       | N/A   |
| 4    | Lower abdomen struck, minor pain                    | 1d4 hours       | N/A   |
| 5    | Side blow, temporary numbness                       | 1d4 hours       | N/A   |
| 6    | Groin strike, slight swelling                       | 1d4 hours       | N/A   |
| 7    | Kidney impact, stinging pain                        | 1d4 hours       | N/A   |
| 8    | Abdominal blow, moderate discomfort                 | 1d4 hours       | N/A   |
| 9    | Organ damage, risk of complications                 | 1d4 days        | N/A   |
| 10   | Internal bleeding, potential for infection          | 1d4 days        | N/A   |
| 11   | Ruptured organ, severe pain                         | 1d4 weeks       | N/A   |
| 12   | Abdominal cavity breached, severe internal injuries | 1d4 weeks       | N/A   |
| 13   | Critical hit, vital organ rupture                   | Instant death   | N/A   |
| 14   | Critical hit, abdominal obliteration                | Instant death   | N/A   |
| 15   | Critical hit, massive internal hemorrhage           | Instant death   | N/A   |
| 16   | Critical hit, abdominal explosion                   | Instant death   | N/A   |
| 17   | Critical hit, instant abdominal disintegration      | Instant death   | N/A   |
| 18   | Critical hit, abdominal vaporization                | Instant death   | N/A   |
| 19   | Critical hit, instant abdominal implosion           | Instant death   | N/A   |
| 20   | Critical hit, abdominal annihilation                | Instant death   | N/A   |
    """,
    """
| Roll | Injury Description                                  | Recovery Time   | Scars |
|------|-----------------------------------------------------|-----------------|-------|
| 1    | Neck graze, minor pain and discomfort               | 1d4 hours       | N/A   |
| 2    | Throat hit, momentary choking sensation             | 1d4 hours       | N/A   |
| 3    | Neck blow, temporary loss of breath                 | 1d4 hours       | N/A   |
| 4    | Collarbone impact, slight discomfort                | 1d4 hours       | N/A   |
| 5    | Jaw struck, temporary jaw numbness                  | 1d4 hours       | N/A   |
| 6    | Neck muscle hit, slight pain                        | 1d4 hours       | N/A   |
| 7    | Adam's apple impact, painful swallowing             | 1d4 hours       | N/A   |
| 8    | Neck shock, moderate discomfort                     | 1d4 hours       | N/A   |
| 9    | Choking risk, risk of complications                 | 1d4 days        | N/A   |
| 10   | Collarbone fracture, potential for deformity        | 1d4 days        | N/A   |
| 11   | Severe neck injury, difficulty in breathing         | 1d4 weeks       | N/A   |
| 12   | Neck fracture, severe pain                          | 1d4 weeks       | N/A   |
| 13   | Critical hit, trachea rupture                       | Instant death   | N/A   |
| 14   | Critical hit, neck obliteration                     | Instant death   | N/A   |
| 15   | Critical hit, severe internal bleeding              | Instant death   | N/A   |
| 16   | Critical hit, neck explosion                        | Instant death   | N/A   |
| 17   | Critical hit, instant neck disintegration           | Instant death   | N/A   |
| 18   | Critical hit, neck vaporization                     | Instant death   | N/A   |
| 19   | Critical hit, instant neck implosion                | Instant death   | N/A   |
| 20   | Critical hit, neck annihilation                     | Instant death   | N/A   |
    """,
    """
| Roll | Injury Description                                  | Recovery Time   | Scars             |
|------|-----------------------------------------------------|-----------------|-------------------|
| 1    | Facial graze, minor pain and discomfort             | 1d4 hours       | Light scar        |
| 2    | Superficial cheek cut, slight bleeding              | 1d4 hours       | Small scar        |
| 3    | Lip nicked, minor pain and bleeding                 | 1d4 hours       | Tiny scar         |
| 4    | Nostril scratched, minor irritation                 | 1d4 hours       | Faint scar        |
| 5    | Eyebrow cut, minor blood and discomfort             | 1d4 hours       | Light scar        |
| 6    | Chin scratched, slight bleeding                     | 1d4 hours       | Small scar        |
| 7    | Jaw cut, stinging pain and minor bleeding           | 1d4 hours       | Tiny scar         |
| 8    | Forehead gash, bleeding and moderate pain           | 1d4 hours       | Faint scar        |
| 9    | Eye injured, risk of blindness                      | 1d4 days        | Disfiguring scar  |
| 10   | Deep facial wound, potential scarring               | 1d4 days        | Visible scar      |
| 11   | Skull fracture, severe headache                     | 1d4 weeks       | Permanent damage  |
| 12   | Head gash, risk of infection                        | 1d4 weeks       | Deep scar         |
| 13   | Critical hit, brain damage                          | Instant death   | N/A               |
| 14   | Critical hit, facial disfigurement                  | Instant death   | N/A               |
| 15   | Critical hit, severed nerve                         | Instant death   | N/A               |
| 16   | Critical hit, eye punctured                         | Instant death   | N/A               |
| 17   | Critical hit, shattered jaw                         | Instant death   | N/A               |
| 18   | Critical hit, facial collapse                       | Instant death   | N/A               |
| 19   | Critical hit, extreme blood loss                    | Instant death   | N/A               |
| 20   | Critical hit, facial mutilation                     | Instant death   | N/A               |
    """,
    """
| Roll | Injury Description                                      | Recovery Time   | Scars             |
|------|---------------------------------------------------------|-----------------|-------------------|
| 1    | Surface bruise, mild discomfort                         | 1d4 hours       | N/A               |
| 2    | Lower back hit, temporary stiffness                     | 1d4 hours       | N/A               |
| 3    | Mid-back blow, momentary pain                           | 1d4 hours       | N/A               |
| 4    | Upper back impact, mild soreness                        | 1d4 hours       | N/A               |
| 5    | Side strike, brief numbness                             | 1d4 hours       | N/A               |
| 6    | Spine hit, slight discomfort                            | 1d4 hours       | N/A               |
| 7    | Kidney shock, sharp pain                                | 1d4 hours       | N/A               |
| 8    | Back thump, moderate discomfort                         | 1d4 hours       | N/A               |
| 9    | Spinal strain, risk of complications                    | 1d4 days        | N/A               |
| 10   | Vertebral fracture, potential nerve damage              | 1d4 days        | N/A               |
| 11   | Severe back injury, difficulty in movement              | 1d4 weeks       | N/A               |
| 12   | Disc herniation, severe pain                            | 1d4 weeks       | N/A               |
| 13   | Critical hit, spinal cord damage                        | Instant death   | N/A               |
| 14   | Critical hit, back obliteration                         | Instant death   | N/A               |
| 15   | Critical hit, catastrophic internal damage              | Instant death   | N/A               |
| 16   | Critical hit, vertebral explosion                       | Instant death   | N/A               |
| 17   | Critical hit, instant back disintegration               | Instant death   | N/A               |
| 18   | Critical hit, back vaporization                         | Instant death   | N/A               |
| 19   | Critical hit, instant back implosion                    | Instant death   | N/A               |
| 20   | Critical hit, back annihilation                         | Instant death   | N/A               |
    """,


    
]

tables_titles = [
    "Impact in the Head",
    "Impact in the Torso",
    "Impact in the Arms",
    "Impact in the Legs",
    "Impact on Abdomen",
    "Impact on Neck",
    "Impact on Face",
    "Impact on the Back",
]

def parse_tables(table):
    
    latex_table = f'\\begin{{description}}[labelwidth=1.5em, leftmargin=*, itemsep=0.4em]\n'
    
    # Split the table by new lines and remove the first two lines (header and separator)
    lines = table.strip().split('\n')[2:]

    # Iterate through each row
    for line in lines:
        # Split by '|' and remove extra spaces
        columns = [col.strip() for col in line.split('|') if col.strip()]
        
        if len(columns) == 4:
            roll, injury_description, recovery_time, scars = columns
            latex_table += f'    \\item[{roll} -] {injury_description} \\textit{{Recovery Time:}} {recovery_time}. \\textit{{Scars:}} {scars}.\n'
        else:
            print("Invalid row format")
    
    latex_table += f'\end{{description}}'
    
    print(f"{latex_table}")

# Iterate over each table, passing it to the parse_tables function
for table in md_tables:
    # Print the title
    print(f'\n\n\n\subsection{{{tables_titles[md_tables.index(table)]}}}')
    parse_tables(table)  # Replace with your actual table)
