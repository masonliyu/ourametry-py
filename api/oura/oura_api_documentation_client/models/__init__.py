"""Contains all the data models used in inputs/outputs"""

from .activity_contributors import ActivityContributors
from .create_webhook_subscription_request import CreateWebhookSubscriptionRequest
from .daily_activity_model import DailyActivityModel
from .daily_cardiovascular_age_model import DailyCardiovascularAgeModel
from .daily_readiness_model import DailyReadinessModel
from .daily_resilience_model import DailyResilienceModel
from .daily_sleep_model import DailySleepModel
from .daily_sp_o2_aggregated_values_model import DailySpO2AggregatedValuesModel
from .daily_sp_o2_model import DailySpO2Model
from .daily_stress_model import DailyStressModel
from .daily_stress_summary import DailyStressSummary
from .enhanced_tag_model import EnhancedTagModel
from .ext_api_v2_data_type import ExtApiV2DataType
from .heart_rate_model import HeartRateModel
from .heart_rate_source import HeartRateSource
from .http_validation_error import HTTPValidationError
from .long_term_resilience_level import LongTermResilienceLevel
from .moment_mood import MomentMood
from .moment_type import MomentType
from .multi_document_response_daily_activity_model import MultiDocumentResponseDailyActivityModel
from .multi_document_response_daily_cardiovascular_age_model import MultiDocumentResponseDailyCardiovascularAgeModel
from .multi_document_response_daily_readiness_model import MultiDocumentResponseDailyReadinessModel
from .multi_document_response_daily_resilience_model import MultiDocumentResponseDailyResilienceModel
from .multi_document_response_daily_sleep_model import MultiDocumentResponseDailySleepModel
from .multi_document_response_daily_sp_o2_model import MultiDocumentResponseDailySpO2Model
from .multi_document_response_daily_stress_model import MultiDocumentResponseDailyStressModel
from .multi_document_response_enhanced_tag_model import MultiDocumentResponseEnhancedTagModel
from .multi_document_response_rest_mode_period_model import MultiDocumentResponseRestModePeriodModel
from .multi_document_response_ring_configuration_model import MultiDocumentResponseRingConfigurationModel
from .multi_document_response_session_model import MultiDocumentResponseSessionModel
from .multi_document_response_sleep_model import MultiDocumentResponseSleepModel
from .multi_document_response_sleep_time_model import MultiDocumentResponseSleepTimeModel
from .multi_document_response_tag_model import MultiDocumentResponseTagModel
from .multi_document_response_vo2_max_model import MultiDocumentResponseVO2MaxModel
from .multi_document_response_workout_model import MultiDocumentResponseWorkoutModel
from .personal_info_response import PersonalInfoResponse
from .readiness_contributors import ReadinessContributors
from .readiness_summary import ReadinessSummary
from .resilience_contributors import ResilienceContributors
from .rest_mode_episode import RestModeEpisode
from .rest_mode_period_model import RestModePeriodModel
from .ring_color import RingColor
from .ring_configuration_model import RingConfigurationModel
from .ring_design import RingDesign
from .ring_hardware_type import RingHardwareType
from .sample_model import SampleModel
from .session_model import SessionModel
from .sleep_algorithm_version import SleepAlgorithmVersion
from .sleep_contributors import SleepContributors
from .sleep_model import SleepModel
from .sleep_time_model import SleepTimeModel
from .sleep_time_recommendation import SleepTimeRecommendation
from .sleep_time_status import SleepTimeStatus
from .sleep_time_window import SleepTimeWindow
from .sleep_type import SleepType
from .tag_model import TagModel
from .time_series_response_heart_rate_model import TimeSeriesResponseHeartRateModel
from .update_webhook_subscription_request import UpdateWebhookSubscriptionRequest
from .validation_error import ValidationError
from .vo2_max_model import VO2MaxModel
from .webhook_operation import WebhookOperation
from .webhook_subscription_model import WebhookSubscriptionModel
from .workout_intensity import WorkoutIntensity
from .workout_model import WorkoutModel
from .workout_source import WorkoutSource

__all__ = (
    "ActivityContributors",
    "CreateWebhookSubscriptionRequest",
    "DailyActivityModel",
    "DailyCardiovascularAgeModel",
    "DailyReadinessModel",
    "DailyResilienceModel",
    "DailySleepModel",
    "DailySpO2AggregatedValuesModel",
    "DailySpO2Model",
    "DailyStressModel",
    "DailyStressSummary",
    "EnhancedTagModel",
    "ExtApiV2DataType",
    "HeartRateModel",
    "HeartRateSource",
    "HTTPValidationError",
    "LongTermResilienceLevel",
    "MomentMood",
    "MomentType",
    "MultiDocumentResponseDailyActivityModel",
    "MultiDocumentResponseDailyCardiovascularAgeModel",
    "MultiDocumentResponseDailyReadinessModel",
    "MultiDocumentResponseDailyResilienceModel",
    "MultiDocumentResponseDailySleepModel",
    "MultiDocumentResponseDailySpO2Model",
    "MultiDocumentResponseDailyStressModel",
    "MultiDocumentResponseEnhancedTagModel",
    "MultiDocumentResponseRestModePeriodModel",
    "MultiDocumentResponseRingConfigurationModel",
    "MultiDocumentResponseSessionModel",
    "MultiDocumentResponseSleepModel",
    "MultiDocumentResponseSleepTimeModel",
    "MultiDocumentResponseTagModel",
    "MultiDocumentResponseVO2MaxModel",
    "MultiDocumentResponseWorkoutModel",
    "PersonalInfoResponse",
    "ReadinessContributors",
    "ReadinessSummary",
    "ResilienceContributors",
    "RestModeEpisode",
    "RestModePeriodModel",
    "RingColor",
    "RingConfigurationModel",
    "RingDesign",
    "RingHardwareType",
    "SampleModel",
    "SessionModel",
    "SleepAlgorithmVersion",
    "SleepContributors",
    "SleepModel",
    "SleepTimeModel",
    "SleepTimeRecommendation",
    "SleepTimeStatus",
    "SleepTimeWindow",
    "SleepType",
    "TagModel",
    "TimeSeriesResponseHeartRateModel",
    "UpdateWebhookSubscriptionRequest",
    "ValidationError",
    "VO2MaxModel",
    "WebhookOperation",
    "WebhookSubscriptionModel",
    "WorkoutIntensity",
    "WorkoutModel",
    "WorkoutSource",
)
