from indivo.serializers import DataModelSerializers
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.data_models.options import DataModelOptions
from indivo.rdf.rdf import PatientGraph

SNOMED_URI="http://purl.bioontology.org/ontology/SNOMEDCT/"
BP_METHOD_URI="http://smartplatforms.org/terms/codes/BloodPressureMethod#"
LOINC_URI="http://purl.bioontology.org/ontology/LNC/"

BP_POSITION_IDS = [
    '40199007', # Supine
    '33586001', # Sitting
    '10904000', # Standing
]

BP_SITE_IDS = [
    '61396006',  # Left thigh
    '368209003', # Right arm
    '11207009',  # Right thigh
    '368208006', # Left arm
]

BP_METHODS = [
    'invasive',
    'palpation',
    'machine',
    'auscultation',
]

VITAL_SIGN_IDS = {
    'bp_diastolic': ['8462-4'],      # Intravascular diastolic
    'bp_systolic': ['8480-6'],       # Intravascular systolic
    'bmi': ['39156-5'],              # Body mass index
    'heart_rate': ['8867-4'],        # Heart rate
    'height': ['8306-3',             # Body height (lying)
               '8302-2'],            # Body height
    'oxygen_saturation': ['2710-2'], # Oxygen saturation
    'resp_rate': ['9279-1'],         # Respiration rate
    'temperature': ['8310-5'],       # Body temperature
    'weight': ['3141-9'],            # Body weight
    'head_circ': ['8287-5'] # Head circumference 
    }

UNITS = {
    'bp': ['mm[Hg]'],
    'bmi': ['kg/m2'],
    'heart_rate': ['{beats}/min'],
    'height': ['m'],
    'oxygen_saturation': ['%{HemoglobinSaturation}'],
    'resp_rate': ['{breaths}/min'],
    'temperature': ['Cel'],
    'weight': ['kg'],
    'head_circ': ['cm'],
}


class VitalsSerializers(DataModelSerializers):
    def to_rdf(query, record=None, carenet=None):
        if not record:
            record = carenet.record

        graph = PatientGraph(record)
        resultOrder = graph.addVitalsList(query.results.iterator(), True if query.limit else False)
        graph.addResponseSummary(query, resultOrder)
        return graph.toRDF()

class VitalsOptions(DataModelOptions):
    model_class_name = 'VitalSigns'
    serializers = VitalsSerializers
    field_validators = {
        'date': [NonNullValidator()],
        
        'bp_position_code_system': [ExactValueValidator(SNOMED_URI, nullable=True)],
        'bp_position_code_identifier': [ValueInSetValidator(BP_POSITION_IDS, nullable=True)],
        'bp_site_code_system': [ExactValueValidator(SNOMED_URI, nullable=True)],
        'bp_site_code_identifier': [ValueInSetValidator(BP_SITE_IDS, nullable=True)],
        'bp_method_code_system': [ExactValueValidator(BP_METHOD_URI, nullable=True)],
        'bp_method_code_identifier': [ValueInSetValidator(BP_METHODS, nullable=True)],
        'bp_diastolic_unit': [ValueInSetValidator(UNITS['bp'], nullable=True)],
        'bp_diastolic_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'bp_diastolic_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['bp_diastolic'], nullable=True)],
        'bp_systolic_unit': [ValueInSetValidator(UNITS['bp'], nullable=True)],
        'bp_systolic_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'bp_systolic_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['bp_systolic'], nullable=True)],

        'bmi_unit': [ValueInSetValidator(UNITS['bmi'], nullable=True)],
        'bmi_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'bmi_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['bmi'], nullable=True)],
       
        'heart_rate_unit': [ValueInSetValidator(UNITS['heart_rate'], nullable=True)],
        'heart_rate_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'heart_rate_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['heart_rate'], nullable=True)],

        'height_unit': [ValueInSetValidator(UNITS['height'], nullable=True)],
        'height_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'height_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['height'], nullable=True)],

        'oxygen_saturation_unit': [ValueInSetValidator(UNITS['oxygen_saturation'], nullable=True)],
        'oxygen_saturation_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'oxygen_saturation_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['oxygen_saturation'], nullable=True)],

        'respiratory_rate_unit': [ValueInSetValidator(UNITS['resp_rate'], nullable=True)],
        'respiratory_rate_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'respiratory_rate_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['resp_rate'], nullable=True)],

        'temperature_unit': [ValueInSetValidator(UNITS['temperature'], nullable=True)],
        'temperature_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'temperature_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['temperature'], nullable=True)],

        'head_circ_unit': [ValueInSetValidator(UNITS['head_circ'], nullable=True)],
        'head_circ_name_code_system': [ExactValueValidator(LOINC_URI, nullable=True)],
        'head_circ_name_code_identifier': [ValueInSetValidator(VITAL_SIGN_IDS['head_circ'], nullable=True)],

        }

