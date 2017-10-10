import urllib3

import feersum_nlu
from feersum_nlu.rest import ApiException

# Configure API key authorization: APIKeyHeader
feersum_nlu.configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'

# feersum_nlu.configuration.host = "http://127.0.0.1:8100/nlu/v2"
feersum_nlu.configuration.host = "http://nlu.playground.feersum.io:8100/nlu/v2"

# wm_instance_name = 'feers_wm_eng'
# We'll use the built-in manifolds, not the ones defined below!
# # === Word manifold to use ===
# print("Create the word manifold model:")
# wm_api_instance = feersum_nlu.WordManifoldsApi()
# wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, desc="Test word manifold.",
#                                               load_from_store=False, input_file="glove.6B.50d.trimmed.txt")
# # wm_create_details = feersum_nlu.CreateDetails(name=wm_instance_name, load_from_store=True)
# wm_api_response = wm_api_instance.word_manifold_create(wm_create_details)
# print(" type(wm_api_response)", type(wm_api_response))
# print(" wm_api_response", wm_api_response)
# print()
# # === ===


api_instance = feersum_nlu.FaqMatchersApi()

instance_name = 'test_faq_mtchr'

create_details = feersum_nlu.CreateDetails(name=instance_name, desc="Test FAQ matcher.", load_from_store=False)

# The training samples.
labelled_text_sample_list = []
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How do I claim?",
                                                                label="claim"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe moet ek eis?",
                                                                label="claim"))

labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="How do I get a quote?",
                                                                label="quote"))
labelled_text_sample_list.append(feersum_nlu.LabelledTextSample(text="Hoe kan ek 'n prys kry?",
                                                                label="quote"))

# Use default English manifold.
# train_details = feersum_nlu.TrainDetails(immediate_mode=True)
# OR
# Use specified single manifold; the language defaults to English.
# train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold=wm_instance_name)
# OR
# Use specified list of manifolds for multiple languaages.
word_manifold_list = [feersum_nlu.LabeledWordManifold('eng', 'feers_wm_eng'),
                      feersum_nlu.LabeledWordManifold('afr', 'feers_wm_afr'),
                      feersum_nlu.LabeledWordManifold('xho', 'feers_wm_xho'),
                      feersum_nlu.LabeledWordManifold('nso', 'feers_wm_nso')]

train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold_list=word_manifold_list)
# train_details = feersum_nlu.TrainDetails(immediate_mode=True, word_manifold_list=word_manifold_list)

text_input = feersum_nlu.TextInput("Waar kan ek 'n prys kry?")

print()

try:
    print("Create the FAQ matcher:")
    api_response = api_instance.faq_matcher_create(create_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Del the training samples of the FAQ matcher:")
    api_response = api_instance.faq_matcher_del_training_samples(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Add training samples to the FAQ matcher:")
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Train the FAQ matcher:")
    api_response = api_instance.faq_matcher_train(instance_name, train_details)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of all loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details_all()
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Get the details of specific named loaded FAQ matcher:")
    api_response = api_instance.faq_matcher_get_details(instance_name)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()

    print("Match a question:")
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    print(" type(api_response)", type(api_response))
    print(" api_response", api_response)
    print()
except ApiException as e:
    print("Exception when calling an FAQ matcher operation: %s\n" % e)
except urllib3.exceptions.MaxRetryError:
    print("Connection MaxRetryError!")
