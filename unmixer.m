% (c) Mohammad Mofrad, 2018
% (e) mohammad.hmofrad@pitt.edu

clear
clc
n = 1;
base1 = '../sounds/dataset/far/mohammad/';
files1 = ["1_play_my_oldies_playlist.wav", "2_sing_A_Christmas_carol.wav", "3_play_the_top_songs_this_week.wav", "4_what's_on_my_calendar_for_today.wav", "5_add_an_event_to_my_calendar.wav", "6_give_me_my_flash_briefing.wav", "7_what's_my_commute_like.wav", "8_discover_my_smart_home_devices.wav", "9_show_me_travel_videos_on_YouTube.wav", "10_what_can_you_show_me.wav", "11_play_my_playlist_on_Spotify.wav", "12_answer_the_call_for_me.wav", "13_read_recorded_messages_from_this_morning.wav", "14_ask_Uber_to_request_a_ride.wav", "15_will_I_need_an_umbrella_today.wav", "16_what_action_movies_are_playing_tonight.wav", "17_find_the_address_for_Bank_of_America.wav", "18_tell_me_a_new_joke.wav", "19_how_do_you_spell_cow.wav", "20_turn_the_lights_to_soft_white.wav", "21_when_am_I_going_to_die.wav", "22_the_quick_brown_fox_jumps_over_the_lazy_dog.wav"];

base1 = '../sounds/dataset/near/mohammad/';

files1 = ["1_stop_the_song.wav", "2_what_song_is_this.wav", "3_set_sleep_timer_for_5_hours.wav", "4_cancel_sleep_timer.wav", "5_repeat_this_song.wav", "6_play_some_music.wav", "7_paly_the_album_speak_now.wav", "8_add_an_event_to_my_calendar.wav", "9_what's_the_news.wav", "10_turn_on_the_lights.wav", "11_set_the_temperature_to_41.wav", "12_call_mom.wav", "13_what's_on_my_shopping_list.wav", "14_tell_me_a_joke.wav", "15_make_an_animal_noise.wav"];

%n = 1;
f1 = strcat(base1, files1(n));
[y1, fs1] = audioread(f1);
y1 = mean(y1,2);


base2 = '../sounds/dataset/far/mina/';
files2 = ["1_turn_up_the_volume.wav", "2_turn_down_the_volume.wav", "3_stop_playing_music_for_5_minutes.wav", "4_add_this_song_to_my_Prime_Music_library.wav", "5_set_a_repeating_alarm_for_6_a.m._weekdays.wav", "6_set_a_second_timer_for_10_minutes.wav", "7_what's_in_the_news.wav", "8_what's_the_extended_forecast_for_Las_Vegas.wav", "9_put_get_an_oil_change_on_my_to-do_list.wav", "10_set_the_volume_to_5.wav", "11_show_the_living_room_camera.wav", "12_read_me_my_Kindle_book.wav", "13_wake_me_up_at_7_in_the_morning.wav", "14_when's_my_next_alarm.wav", "15_what_are_my_notifications.wav", "16_remind_me_to_check_the_oven_in_5_minutes.wav", "17_find_me_a_nearby_pizza_restaurant.wav", "18_roll_a_26-sided_die.wav", "19_what's_the_definition_of_cow.wav", "20_turn_off_the_living_room_lights.wav", "21_give_me_an_Easter_egg.wav", "22_pack_my_box_with_5_dozen_liquor_jugs.wav"];

base2 = '../sounds/dataset/near/mina/';
files2 = ["1_set_volume_up.wav", "2_who_is-this_artist.wav", "3_stop_playing_music_for_5_minutes.wav","4_pause_the_music.wav", "5_stop_shuffling_music.wav", "6_play_the_song.wav" ,"7_play_songs_by_taylor_swift.wav", "8_what's_the_weather_like_today.wav", "9_will_it_rain_today.wav", "10_lock_the_front_door.wav", "11_turn_on_the_tv.wav", "12_play_messages.wav", "13_where_is_my_stuff.wav", "14_flip_a_coin.wav", "15_lagh_at_me.wav"];



f2 = strcat(base2, files2(n));
[y2, fs2] = audioread(f2);
%y2 = y2(:,1);
%y2 = y2';
y2 = mean(y2,2);


len1 = length(y1);
len2 = length(y2);
if(length(y1) > length(y2))
    len = length(y1);
    y = zeros(len,2);
    y(1:len1,1) = y1(1:len1);    
    y(1:len2,2) = y2(1:len2);    
else
    len = length(y2);
    y = zeros(len,2);
    y(1:len1,1) = y1(1:len1);    
    y(1:len2,2) = y2(1:len2);    
end


y = prewhiten(y);
q = 2;
Mdl = rica(y, q, 'NonGaussianityIndicator', ones(q,1));
unmixed = transform(Mdl,y);

audiowrite('out1.wav', unmixed(:,1), fs1);
audiowrite('out2.wav', unmixed(:,2), fs2);
