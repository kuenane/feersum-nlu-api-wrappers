# coding: utf-8

# flake8: noqa
"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.14
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into model package
from feersum_nlu.models.class_label import ClassLabel
from feersum_nlu.models.class_label_list import ClassLabelList
from feersum_nlu.models.class_label_pair import ClassLabelPair
from feersum_nlu.models.create_details import CreateDetails
from feersum_nlu.models.dashboard_detail import DashboardDetail
from feersum_nlu.models.dashboard_model_detail import DashboardModelDetail
from feersum_nlu.models.date import Date
from feersum_nlu.models.date_list import DateList
from feersum_nlu.models.duckling_ent_create_details import DucklingEntCreateDetails
from feersum_nlu.models.duckling_instance_detail import DucklingInstanceDetail
from feersum_nlu.models.duckling_instance_detail_list import DucklingInstanceDetailList
from feersum_nlu.models.entity import Entity
from feersum_nlu.models.entity_list import EntityList
from feersum_nlu.models.instance_detail import InstanceDetail
from feersum_nlu.models.instance_detail_list import InstanceDetailList
from feersum_nlu.models.labeled_word_manifold import LabeledWordManifold
from feersum_nlu.models.labelled_text_sample import LabelledTextSample
from feersum_nlu.models.labelled_text_sample_list import LabelledTextSampleList
from feersum_nlu.models.lr4_create_details import Lr4CreateDetails
from feersum_nlu.models.lr4_instance_detail import Lr4InstanceDetail
from feersum_nlu.models.lr4_instance_detail_list import Lr4InstanceDetailList
from feersum_nlu.models.model_params import ModelParams
from feersum_nlu.models.new_word import NewWord
from feersum_nlu.models.new_word_list import NewWordList
from feersum_nlu.models.regex_ent_create_details import RegexEntCreateDetails
from feersum_nlu.models.regex_instance_detail import RegexInstanceDetail
from feersum_nlu.models.regex_instance_detail_list import RegexInstanceDetailList
from feersum_nlu.models.scored_label import ScoredLabel
from feersum_nlu.models.scored_label_list import ScoredLabelList
from feersum_nlu.models.sentiment import Sentiment
from feersum_nlu.models.similarity_ent_create_details import SimilarityEntCreateDetails
from feersum_nlu.models.similarity_instance_detail import SimilarityInstanceDetail
from feersum_nlu.models.similarity_instance_detail_list import SimilarityInstanceDetailList
from feersum_nlu.models.text_clsfr_create_details import TextClsfrCreateDetails
from feersum_nlu.models.text_clsfr_instance_detail import TextClsfrInstanceDetail
from feersum_nlu.models.text_clsfr_instance_detail_list import TextClsfrInstanceDetailList
from feersum_nlu.models.text_input import TextInput
from feersum_nlu.models.total_samples import TotalSamples
from feersum_nlu.models.train_details import TrainDetails
from feersum_nlu.models.wm_create_details import WmCreateDetails
from feersum_nlu.models.wm_instance_detail import WmInstanceDetail
from feersum_nlu.models.wm_instance_detail_list import WmInstanceDetailList
from feersum_nlu.models.word_and_distance import WordAndDistance
from feersum_nlu.models.word_and_distance_list import WordAndDistanceList
from feersum_nlu.models.word_and_threshold import WordAndThreshold
